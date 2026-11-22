import subprocess, time, sys
from data import icons, messages, options

no_arg = {
    1: "-Syu", 2: "-Sy",
    9: "-Q", 15: "-Qdt"
}
arg = {
    3: "-S", 4: "-U", 5: "-Sw",
    6: "-Qs", 7: "-Qi", 8: "-Ql", 
    10: "-Ss", 11: "-Si", 12: "-R", 
    13: "-Rs", 14: "-Rns"
}

print(f"{icons[7]} \033[36mPacman {messages[3]}\033[0m {icons[7]}\n")
print(messages[1])
for i, option in options.items():
    print(f"{i}. {option[0]}")
choice_input = input("> ")

def exec_pacman():
    if choice_input.isnumeric():
        choice = int(choice_input)
        if choice <= 15 and choice >= 1:
            if choice == 1 or choice == 2 or choice == 9 or choice == 15:
                def exec_no_args():
                    if choice == 1:
                        time.sleep(0.2)
                        print(icons[6] + " \033[1;4;31mAre you sure? [y/n]\033[0m " + icons[6])
                        update_choice_input = input("> ")
                        if type(update_choice_input) == str:
                            update_choice = str(update_choice_input)
                            if update_choice == "" or update_choice == "y" or update_choice == "Y":
                                print(options[1][1])
                                subprocess.run([
                                    "sudo", "pacman", no_arg[1]
                                ])
                            elif update_choice == "n" or update_choice == "N":
                                print(f"{messages[4]}")
                            else:
                                print(f"{icons[9]} {messages[2]}")
                        else:
                            print(f"{icons[9]} {messages[2]}")
                    else:
                        print(options[choice][1])
                        subprocess.run([
                            "sudo", "pacman", no_arg[choice]
                        ])
                exec_no_args()
            else:
                def exec_with_args():
                    print(options[choice][1])
                    print(options[choice][2])
                    package = input("> ")
                    if type(package) == str:
                        pkgs = package.split()
                        if not pkgs:
                            print(f"{icons[9]} {messages[2]}")
                            return
                        subprocess.run([
                            "sudo", "pacman", arg[choice], *pkgs
                        ])
                    else:
                        print(f"{icons[9]} {messages[2]}")
                exec_with_args()
        else:
            print(f"{icons[9]} {messages[2]}")
    else:
        print(f"{icons[9]} {messages[2]}")
exec_pacman()
