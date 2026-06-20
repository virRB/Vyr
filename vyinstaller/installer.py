from pathlib import Path
import shutil
import winreg

BASE_DIR = Path(__file__).parent

VYR_SRC = BASE_DIR / "Vyr"
BACKEND_SRC = BASE_DIR / "backend.py"
BAT_SRC = BASE_DIR / "vy.bat"


USER_HOME = Path.home()
INSTALL_DIR = USER_HOME / "VyrBackend"

print("Installing VyScript...")

if INSTALL_DIR.exists():
    print("Removing old installation...")
    shutil.rmtree(INSTALL_DIR)

INSTALL_DIR.mkdir(parents=True, exist_ok=True)


if VYR_SRC.exists():
    shutil.copytree(VYR_SRC, INSTALL_DIR / "Vyr")
else:
    print("Missing Vyr folder")

if BACKEND_SRC.exists():
    shutil.copy2(BACKEND_SRC, INSTALL_DIR / "backend.py")
else:
    print("Missing backend.py")

if BAT_SRC.exists():
    shutil.copy2(BAT_SRC, INSTALL_DIR / "vy.bat")
else:
    print("Missing vy.bat")

print("Files installed to:", INSTALL_DIR)


def add_to_path(path: str):
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        "Environment",
        0,
        winreg.KEY_READ | winreg.KEY_WRITE
    )

    try:
        current_path, _ = winreg.QueryValueEx(key, "PATH")
    except FileNotFoundError:
        current_path = ""

    paths = [p for p in current_path.split(";") if p]

    if path in paths:
        print("PATH already clean.")
        winreg.CloseKey(key)
        return

    paths.append(path)
    updated_path = ";".join(paths)

    winreg.SetValueEx(key, "PATH", 0, winreg.REG_EXPAND_SZ, updated_path)
    winreg.CloseKey(key)

    print("Added to PATH:", path)

add_to_path(str(INSTALL_DIR))

print("\n✔ VyScript installed successfully!")
print("Restart terminal to use 'vy'")

input("> ")