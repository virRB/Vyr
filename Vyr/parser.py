#parser
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


in_ais = False
in_if = False
in_func = False
nest = 0
modules = []
headers = ["def", "if", "class"]
vars = []
funcs = []

runtime = os.path.join(BASE_DIR, "runitme.py")
test = os.path.join(BASE_DIR, "TEST.vyr")


def write_into(what):
    open(runtime, "a").write(what + "\n")


def clear():
    open(runtime, "w").write("")


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
    global in_ais, in_if, in_func, nest, modules, vars

    output = ""


    for module in modules:
        if line.startswith(module):
            new = line.split(".use -> ")
            output = f"{new[0]}.{new[1]}"
            call = True

    for var in vars:
        if line.startswith(var):
            output = line

    if ver == "recurse":
        pass

    if line == "}":
        if in_ais:
            in_ais = False
            output = ""
        elif nest > 0:
            nest -= 1
            output = ""
        else:
            output = ""

    elif in_ais:
        fin = line.replace(",", "")
        output = f"import modules.{fin} as {fin}"
        if fin not in modules:
            modules.append(fin)

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
        splt = line.split(" = ")
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