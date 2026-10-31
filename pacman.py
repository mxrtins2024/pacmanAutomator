import subprocess, time, sys
from data import icons, messages

# Pacman package manager processes
def pacman():
    # [1] Update system
    def update():
        print(icons[6] + " \033[1;4;31mAre you sure? [y/n]\033[0m " + icons[6])
        update_choice_input = input("> ")
        if type(update_choice_input) == str:
            update_choice = str(update_choice_input)
            if update_choice == "" or update_choice == "y" or update_choice == "Y":
                subprocess.run([
                    "sudo", "pacman", "-Syu"
                ])
            elif update_choice == "n"  or update_choice == "N":
                print(f"{messages[4]}")
            else:
                print(f"{icons[9]} {messages[2]}")
        else:
            print(f"{icons[9]} {messages[2]}")
    def database():
        subprocess.run([
            "sudo", "pacman", "-Sy"
        ])
    # [3] Install package
    def install(package):
        subprocess.run([
            "sudo", "pacman", "-S", package
        ])
    # [4] Install local package
    # package = path
    def install_local(package):
        subprocess.run([
            "sudo", "pacman", "-U", package
        ])
    # [5] Download package without install
    def download_no_install(package):
        subprocess.run([
            "sudo", "pacman", "-Sw", package
        ])
    # [6] Search for already installed package
    def search_installed(package):
        subprocess.run([
            "pacman", "-Qs", package
        ])
    # [7] List detailed info of a installed package
    def list_info_installed(package):
        subprocess.run([
            "sudo", "pacman", "-Qi", package
        ])
    # [8] List download files of a package
    def list_files_downloaded(package):
        subprocess.run([
            "sudo", "pacman", "-Ql", package
        ])
    # [9] List all installed packages in the system
    def list_all():
        subprocess.run([
            "pacman", "-Q"
        ])
    # [10] Search for package in the repository
    def search_repo(package):
        subprocess.run([
            "pacman", "-Ss", package
        ])
    # [11] Show info of a package of the repository
    def info_repo(package):
        subprocess.run([
            "pacman", "-Si", package
        ])
    # [12] Remove installed package
    def remove(package):
        subprocess.run([
            "sudo", "pacman", "-R", package
        ])
    # [13] Remove installed package and dependencies (not used by others)
    def remove_dependencies(package):
        subprocess.run([
            "sudo", "pacman", "-Rs", package
        ])
    # [14] Remove installed package, dependencies and configs
    def remove_all(package):
        subprocess.run([
            "sudo", "pacman", "-Rns", package
        ])
    # [15] List installed packages as dependencies that are no longer necessary
    def list_packages_dependencies_useless():
        subprocess.run([
            "pacman", "-Qdt"
        ])
    # Return
    return update, database, install, install_local, download_no_install, search_installed, list_info_installed, list_files_downloaded, list_all, search_repo, info_repo, remove, remove_dependencies, remove_all, list_packages_dependencies_useless

update, database, install, install_local, download_no_install, search_installed, list_info_installed, list_files_downloaded, list_all, search_repo, info_repo, remove, remove_dependencies, remove_all, list_packages_dependencies_useless = pacman()
# Available processes:
options = {
    1: (
        f" {icons[5]} Update system",
        f"{icons[1]} System update selected"
    ),
    2: (
        f" {icons[5]} Synchronize package databases",
        f"{icons[1]} Synchronize package databases selected"
    ),
    3: (
        f" {icons[0]} Install package",
        f"{icons[1]} Package installation selected",
        f"{icons[0]} {messages[0]} install?"
    ),
    4: (
        f" {icons[0]} Install local package (.pkg.tar.zst)",
        f"{icons[1]} Local package installation selected",
        f"{icons[0]} {messages[0]} install (Enter file path)?"
    ),
    5: (
        f" {icons[0]} Download package without installing it",
        f"{icons[1]} Download package without installing it selected",
        f"{icons[0]} {messages[0]} download?"
    ),
    6: (
        f" {icons[3]} Search for installed package",
        f"{icons[1]} Search for installed package selected",
        f"{icons[3]} {messages[0]} search?"
    ),
    7: (
        f" {icons[3]} List detailed information of installed package",
        f"{icons[1]} Search for installed package selected",
        f"{icons[3]} {messages[0]} search?"
    ),
    8: (
        f" {icons[3]} List downloaded files from a package",
        f"{icons[1]} List downloaded files from a package selected",
        f"{icons[3]} Which downloaded files from a package you want to list?"
    ),
    9: (
        f" {icons[3]} List all downloaded packages of the system",
        f"{icons[1]} List all downloaded packages of the system selected"
    ),
    10: (
        f"{icons[3]} Search package in the repository",
        f"{icons[1]} Search package in the repositoty selected",
        f"{icons[3]} {messages[0]} search?"
    ),
    11: (
        f"{icons[3]} Show info of package in the repository",
        f"{icons[1]} Show info of package in the repository selected",
        f"{icons[3]} {messages[0]} show info?"
    ),
    12: (
        f"{icons[4]} Remove package",
        f"{icons[1]} Remove installed package selected",
        f"{icons[8]} {messages[0]} remove?"
    ),
    13: (
        f"{icons[4]} Remove package and dependencies (not used by others)",
        f"{icons[1]} Remove package and dependencies (not used by others) selected",
        f"{icons[8]} {messages[0]} remove?"
    ),
    14: (
        f"{icons[4]} Remove package, dependencies and configs",
        f"{icons[1]} Remove package, dependencies and configs selected",
        f"{icons[8]} {messages[0]} remove?"
    ),
    15: (
        f"{icons[4]} List installed packages as dependencies that are no longer necessary",
        f"{icons[1]} List installed packages as dependencies that are no longer necessary selected"
    )
}

processes_arg = {
    # 1: update
    # 2: database
    3: install,
    4: install_local,
    5: download_no_install,
    # 6: search_installed
    7: list_info_installed,
    8: list_files_downloaded,
    # 9: list_all
    10: search_repo,
    11: info_repo,
    12: remove,
    13: remove_dependencies,
    14: remove_all
    # 15: list_packages_dependencies_useless
}

# Automator intro and process choice
print(f"{icons[7]} \033[36mPacman {messages[3]}\033[0m {icons[7]}")
print("")
time.sleep(0.2)
print(messages[1])
for i, option in options.items():
    print(f"{i}. {option[0]}")
choice_input = input("> ")

# Execute process selected
def run_process():
    if choice_input.isnumeric():
        choice = int(choice_input)
        if choice > len(options):
            print(f"{icons[9]} {messages[2]}")
        else:
            if choice == 1:
                time.sleep(0.5)
                print(options[1][1])
                update()
            elif choice == 2:
                time.sleep(0.5)
                print(options[2][1])
                database()
            elif choice == 6:
                time.sleep(0.5)
                print(options[6][1])
                search_installed(str(input("> ")))
            elif choice == 9:
                time.sleep(0.2)
                print(options[9][1])
                list_all()
            elif choice == 15:
                time.sleep(0.2)
                print(options[15][1])
                list_packages_dependencies_useless()
            else:
                time.sleep(0.2)
                print(options[choice][1])
                print(options[choice][2])
                processes_arg[choice](str(input("> ")))
    else:
        print(f"{icons[9]} {messages[2]}")
run_process()