import sys
import os
import shutil
import subprocess

SOURCE_ROOT = os.path.join(os.getcwd(), "Vyr")

def spawn_project(name):
    target = os.path.join(os.getcwd(), name)

    if os.path.exists(target):
        print(f"Folder already exists: {target}")
        return

    shutil.copytree(SOURCE_ROOT, target)
    print(f"Spawned project: {target}")


def run_project():
    cwd = os.getcwd()

    parser_path = os.path.join(cwd, "parser.py")
    runtime_path = os.path.join(cwd, "runitme.py")

    print("ARGS:", sys.argv[1:])

    if os.path.exists(parser_path):
        print("🐡The Fish is conjuring your script...")
        subprocess.run([sys.executable, parser_path], cwd=cwd)
    else:
        print("parser.py not found in", cwd)
        return

    if os.path.exists(runtime_path):
        print("🐟Starting Project...")
        subprocess.run([sys.executable, runtime_path], cwd=cwd)
    else:
        print("runitme.py not found in", cwd)


def repl():
    print("Vyr REPL started. Commands: spawn, run, exit")

    while True:
        parts = input("vy> ").strip().split()

        if len(parts) == 0:
            continue

        handle_command(parts)


def handle_command(parts):
    cmd = parts[0]

    if cmd == "spawn":
        if len(parts) < 2:
            print("Usage: vy spawn <name>")
            return
        spawn_project(parts[1])

    elif cmd == "run":
        run_project()

    elif cmd == "start":
        repl()

    elif cmd == "exit":
        exit()

    else:
        print("Unknown command:", cmd)


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print("Usage: vy <start|spawn|run>")
        return

    handle_command(args)


if __name__ == "__main__":
    main()