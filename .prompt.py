from colorama import Fore, Back, Style
from socket import gethostname
from time import strftime
import os
import subprocess


def get_terminal_size():
    """
    Get the terminal width and height.

    Grabbed from http://stackoverflow.com/a/3010495/359284
    """

    import fcntl, termios, struct

    h, w, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))

    return w, h


def generate_section(text, back_color, text_color,
                     previous_back_color=None, text_style="NORMAL"):
    RIGHT_ARROW = u"\u2B80".encode("utf-8")

    back_color = getattr(Back, back_color)
    text_color = getattr(Fore, text_color)
    text_style = getattr(Style, text_style)

    section = back_color

    if previous_back_color:
        fore_color = getattr(Fore, previous_back_color)

        section += fore_color + Style.NORMAL + RIGHT_ARROW

    section += text_color + text_style + " " + text

    return section

time = strftime("%H:%M:%S")
user = os.environ["USER"]
cwd = os.getcwd()

print generate_section(time, "WHITE", "BLACK"),
print generate_section(user, "BLUE", "WHITE", "WHITE", "BRIGHT"),
print generate_section(cwd, "YELLOW", "BLACK", "BLUE", "DIM"),

last_color = "YELLOW"

if "VIRTUAL_ENV" in os.environ:
    virtualenv = os.environ["VIRTUAL_ENV"]
    virtualenv_name = os.path.basename(virtualenv)

    print generate_section(virtualenv_name, "BLUE", "WHITE", last_color,
                           "BRIGHT"),
    last_color = "BLUE"

git_branch = subprocess.Popen(["git", "symbolic-ref", "--short", "HEAD"],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
branch_name, err = git_branch.communicate()

if branch_name:
    unstaged_changes = subprocess.Popen(["git", "diff"],
                                        stderr=subprocess.PIPE,
                                        stdout=subprocess.PIPE)
    needs_staging, _ = unstaged_changes.communicate()

    staged_changes = subprocess.Popen(["git", "diff", "--staged"],
                                        stderr=subprocess.PIPE,
                                        stdout=subprocess.PIPE)
    needs_committing, _ = staged_changes.communicate()

    back_color = "WHITE"
    text_color = "BLACK"
    style = "DIM"

    if needs_staging:
        back_color = "RED"
        text_color = "YELLOW"
        style = "BRIGHT"
    elif needs_committing:
        back_color = "GREEN"
        text_color = "WHITE"
        style = "BRIGHT"

    print generate_section(branch_name.strip(), back_color, text_color,
                           last_color, style),
    last_color = back_color

print generate_section("", "RESET", "RESET", last_color)
print Fore.GREEN + Style.BRIGHT + "$ " + Style.RESET_ALL,
