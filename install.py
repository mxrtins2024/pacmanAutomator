import subprocess, time, os, shutil, sys
from pathlib import Path
from data import messages, icons

source_dir = Path(__file__).resolve().parent
install_dir = Path.home() / ".config" / "pacmanAutomator"
bin_path = Path("/usr/local/bin/syspacman")
scripts = ["pacman.py", "data.py"]
executable = "syspacman"

def install():
    print("[↓] Pacman Automator installer [↓]")
    time.sleep(0.3)
    if os.geteuid() == 0:
        print(f"{icons[6]} Do not run this installer with sudo. Run it as a normal user (it asks for sudo only when needed).")
        sys.exit(1)
    # Check if all required files are in the automator folder
    missing = [f for f in scripts + [executable] if not (source_dir / f).exists()]
    if missing:
        print(f"{icons[6]} Missing files next to the installer: {', '.join(missing)}")
        sys.exit(1)
    if install_dir.exists():
        print(f"{icons[6]} The path '{install_dir}' already exists, remove or rename it before installing")
        sys.exit(1)
    if bin_path.exists():
        print(f"{icons[6]} The file 'syspacman' already exists in '{bin_path}', remove or rename it before installing")
        sys.exit(1)
    # Installation
    try:
        install_dir.mkdir(parents=True)
        for script in scripts:
            shutil.move(str(source_dir / script), str(install_dir / script))
        subprocess.run(["sudo", "mv", str(source_dir / executable), str(bin_path)], check=True)
        subprocess.run(["sudo", "chmod", "+x", str(bin_path)], check=True)
    except (OSError, subprocess.CalledProcessError) as e:
        print(f"{icons[6]} Installation failed: {e}")
        sys.exit(1)
    time.sleep(2)
    print(f"{icons[1]} {messages[6]}")
    time.sleep(1)
    print(f"{icons[10]} {messages[5]} ~/.config/pacmanAutomator")
    time.sleep(1)
    print(f"{icons[11]} {messages[7]} 'syspacman'")
if __name__ == "__main__":
    install()