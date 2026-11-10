import sys, os

messages =  [
    "Which package do you want to",   # 0
    "What do you want to do?",        # 1
    "Invalid option",                 # 2
    "Automator",                      # 3
    "Process aborted",                # 4
    "Source codes are available in ", # 5
    "Installation done!",             # 6
    "To start using, enter"           # 7
]
icons = [
    "⬇️", "✅", "📦", "🔎", "🗑️", "🔄",
    # 0     1     2     3     4     5
    "⚠️", "⚙️", "↪️", "⛔", "📌", "💫"
    # 6     7     8      9     10    11
]

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
        f"{icons[1]} List detailed information of installed package selected",
        f"{icons[3]} {messages[0]} list?"
    ),
    8: (
        f" {icons[3]} List files belonging to installed package",
        f"{icons[1]} List files belonging to installed package selected",
        f"{icons[3]} Which files belonging from a installed package do you want to list?"
    ),
    9: (
        f" {icons[3]} List all downloaded packages of the system",
        f"{icons[1]} List all downloaded packages of the system selected"
    ),
    10: (
        f"{icons[3]} Search for package in repositories",
        f"{icons[1]} Search for package in repositories selected",
        f"{icons[3]} {messages[0]} search?"
    ),
    11: (
        f"{icons[3]} Display repository package information",
        f"{icons[1]} Display repository package information selected",
        f"{icons[3]} {messages[0]} display information?"
    ),
    12: (
        f"{icons[4]} Remove package",
        f"{icons[1]} Remove installed package selected",
        f"{icons[8]} {messages[0]} remove?"
    ),
    13: (
        f"{icons[4]} Remove packages along with unused dependencies",
        f"{icons[1]} Remove packages along with unused dependencies selected",
        f"{icons[8]} {messages[0]} remove?"
    ),
    14: (
        f"{icons[4]} Remove packages, dependencies and configuration files",
        f"{icons[1]} Remove packages, dependencies and configuration files selected",
        f"{icons[8]} {messages[0]} remove?"
    ),
    15: (
        f"{icons[4]} List installed packages as dependencies that are no longer needed",
        f"{icons[1]} List installed packages as dependencies that are no longer needed selected"
    )
}
