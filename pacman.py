import subprocess, time, sys
from data import icons, messages, options

pacman_arg = {
    1: "-Syu", 2: "-Sy", 3: "-S", 4: "-U", 5: "-Sw",
    6: "-Qs", 7: "-Qi", 8: "-Ql", 9: "-Q", 10: "-Ss",
    11: "-Si", 12: "-R", 13: "-Rs", 14: "-Rns", 15: "-Qdt"
}
# 1, 2, 9 and 15

# Automator intro and process choice
print(f"{icons[7]} \033[36mPacman {messages[3]}\033[0m {icons[7]}\n")
time.sleep(0.2)
print(messages[1])
for i, option in options.items():
    print(f"{i}. {option[0]}")
choice_input = input("> ")

def exec_pacman():
    if choice_input.isnumeric():
        choice = int(choice_input)
        if choice > len(pacman_arg):
            print(f"{icons[9]} {messages[2]}")
        else:
            if choice == 1:
                time.sleep(0.5)
                print(icons[6] + " \033[1;4;31mAre you sure? [y/n]\033[0m " + icons[6])
                update_choice_input = input("> ")
                if type(update_choice_input) == str:
                    update_choice = str(update_choice_input)
                    if update_choice == "" or "y" or "Y":
                        print(options[1][1])
                        subprocess.run([
                            "sudo", "pacman", pacman_arg[1]
                        ])
                    elif update_choice == "n" or "N":
                        print(f"{messages[4]}")
                    else:
                        print(f"{icons[9]} {messages[2]}")
                else:
                    print(f"{icons[9]} {messages[2]}")
            elif choice == 2:
                print(options[2][1])
                subprocess.run([
                    "sudo", "pacman", pacman_arg[2]
                ])
            elif choice == 9:
                print(options[9][1])
                subprocess.run([
                    "pacman", pacman_arg[9]
                ])
            elif choice == 15:
                print(options[15][1])
                subprocess.run([
                    "pacman", pacman_arg[15]
                ])
            else:
                print(options[choice][1])
                print(options[choice][2])
                package = input("> ")
                pkgs = package.split()
                if not pkgs:
                    print(f"{icons[9]} {messages[2]}")
                    return
                subprocess.run([
                    "sudo", "pacman", pacman_arg[choice], *pkgs
                ])
    else:
        print(f"{icons[9]} {messages[2]}")
exec_pacman()
