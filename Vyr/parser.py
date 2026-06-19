#parser
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


in_ais = False
in_if = False
in_func = False
wpo = False
nest = 0
modules = []
headers = ["def", "if", "class", "for", "while", "try"]
vars = []
funcs = []
structs = []
in_struct = False

runtime = os.path.join(BASE_DIR, "runitme.py")
test = os.path.join(BASE_DIR, "TEST.vyr")


def write_into(what):
    open(runtime, "a", encoding="utf-8").write(what + "\n")


def clear():
    open(runtime, "w", encoding="utf-8").write("")


clear()


def apply_indent(output, is_block_header=False):
    global nest

    if not output:
        return None


    if is_block_header:
        indent_level = nest - 1 if nest > 0 else 0
    else:
        indent_level = nest

    return ("    " * indent_level) + output


def parse(line, ver):
    line = line.strip()
    call = False
    global in_ais, in_if, in_func, nest, modules, vars, wpo, structs, headers, in_struct

    output = ""


    for module in modules:
        if line.startswith(module):
            new = line.split(".use -> ")
            output = f"{new[0]}.{new[1]}"
            call = True

    for var in vars:
        if line.startswith(var):
            new = line.split(" = ")
            rhs = new[1]
            rhs = parse(rhs, "recurse")
            call = True
            lhs = new[0]
            output = f"{lhs} = {rhs}"

    if line.startswith("return"):
        output = line

    if wpo:
        nest += 1
        wpo = False

    if ver == "recurse" and not (line.endswith(")")) and not (line.startswith("data")):
        output = line

    elif line == "}":
        if in_ais:
            in_ais = False
            output = ""
        elif in_struct:
            nest -= 1
            in_struct = False
            output = "}"
        elif nest > 0:
            nest -= 1
            output = ""
        else:
            output = ""
    elif line == "} otherwise {":
        output = "else:"
        nest -= 1
        wpo = True

    elif line.startswith("data"):
        line = line.replace("data ", "")
        for struct in structs:
            if line.startswith(struct):
                line = line.split(".")
                n = f'["{line[1]}"]'
                output = f"{line[0]}{n}"

    elif line.endswith("]"):
        output = line

    elif in_struct:
        line = line.split(": ")
        output = f'"{line[0]}": {line[1]}'

    elif line.startswith("dat") and line.endswith("{"):
        line = line.replace("dat ", "")
        line = line.replace(" -> {", "")
        output = line + " = {"
        structs.append(line)
        headers.append(line)
        nest += 1
        in_struct = True

    elif line.startswith("} othif") and line.endswith("{"):
        line = line.replace("} othif ", "")
        line = line.replace(" {", "")
        output = f"elif {line}:"
        nest -= 1
        wpo = True

    elif in_ais:
        fin = line.replace(",", "")
        output = f"import modules.{fin} as {fin}"
        if fin not in modules:
            modules.append(fin)

    elif line.startswith("aslongas"):
        line = line.replace("aslongas ", "")
        line = line.replace(" -> {", "")
        condition = line
        output = f"while {condition}:"
        nest += 1

    elif line.startswith("attempt"):
        output = f"try:"
        nest += 1

    elif line == "end":
        output = "break"

    elif line == "skip":
        output = "continue"

    elif line == "} onfail {":
        output = "except:"
        nest -= 1
        wpo = True

    elif line.startswith("alias"):
        if ".pull" in line:
            line = line.split(" -> ")
            if line[0] == "alias.pull":
                output = f"from modules.{line[1]} import {line[2]}"
        elif ".alias" in line:
            line = line.split(" -> ")
            if line[0] == "alias.alias":
                output = f"import modules.{line[1]} as {line[2]}"

    elif line.startswith("for") and line.endswith("{"):
        line = line.replace("for ", "")
        line = line.replace(" {", "")
        line = line.split(" -> ")
        output = f"for {line[0]} in {line[1]}:"
        nest += 1


    elif line.startswith("addInScript"):
        if " -> " in line:
            splt = line.split(" -> ")
            if splt[1] == "{":
                in_ais = True
                output = ""
        else:
            print("Invalid syntax")

    elif line.startswith("var"):
        line = line.replace("var ", "")
        splt = line.split(" = ", 1)
        new = splt[1]
        new = parse(new, "recurse")
        call = True
        output = f"{splt[0]} = {new}"
        vars.append(splt[0])

    elif line.startswith("func"):
        new = line.replace("func", "def")
        new = new.replace(" {", ":")
        output = new
        nest += 1

    elif line.startswith("if"):
        new = line.replace(" {", ":")
        output = new
        nest += 1

    elif line.startswith("@"):
        new = line.replace("@", "#")
        output = new

    elif line.startswith("prnt"):
        output = line.replace("prnt", "print")

    elif line.endswith(")"):
        if not call:
            output = line

    elif line.startswith("public"):
        output = line.replace("public", "global")

    if not output:
        return None

    is_header = any(output.startswith(h) for h in headers)

    output = apply_indent(output, is_header)

    return output


lines = open(test, encoding="utf-8").readlines()


def do_stuff():
    for line in lines:
        thing = parse(line, "normal")
        if not thing:
            continue
        write_into(thing)


do_stuff()
