from pathlib import Path
import shutil
import subprocess
import sys

INSTALL_DIR = Path.home() / "VyrBackend"
TEMPLATE_DIR = INSTALL_DIR / "Vyr"


def spawn_project(name):
    target = Path.home() / name

    if target.exists():
        print(f"Folder already exists: {target}")
        return

    if not TEMPLATE_DIR.exists():
        print(f"Template missing: {TEMPLATE_DIR}")
        return

    shutil.copytree(TEMPLATE_DIR, target)
    print(f"Spawned project: {target}")


def run_project():
    cwd = Path.cwd()

    print(f"Running project from: {cwd}")

    parser_path = cwd / "parser.py"
    runtime_path = cwd / "runitme.py"

    if not parser_path.exists():
        print(f"parser.py not found in {cwd}")
        return

    print("🐡Henry is conjuring your script...")
    subprocess.run([sys.executable, str(parser_path)], cwd=cwd)

    if runtime_path.exists():
        print("🐡Starting Project...")
        subprocess.run([sys.executable, str(runtime_path)], cwd=cwd)
    else:
        print(f"runitme.py not found in {cwd}")


def repl():
    while True:
        parts = input("vy> ").strip().split()

        if not parts:
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
        sys.exit(0)

    else:
        print("Unknown command:", cmd)


def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: vy <spawn|run|start>")
        return

    handle_command(args)


if __name__ == "__main__":
    main()