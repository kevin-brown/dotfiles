from colorama import Fore, Back, Style
from socket import gethostname
from time import strftime
import os
import subprocess

time = strftime("%H:%M:%S")
user = os.environ["USER"]
cwd = os.getcwd()

RIGHT_ARROW = u"\u2B80".encode("utf-8")

print Back.WHITE + Fore.BLACK + Style.NORMAL, time,
print Back.BLUE + Fore.WHITE + RIGHT_ARROW,

print Fore.YELLOW + Style.BRIGHT + user,
print Fore.BLUE + Style.NORMAL + Back.YELLOW + RIGHT_ARROW,

print Fore.BLACK + Style.DIM + cwd,

INVERT_COLOR = Fore.YELLOW

if "VIRTUAL_ENV" in os.environ:
    virtualenv = os.environ["VIRTUAL_ENV"]
    virtualenv_name = os.path.basename(virtualenv)

    print Style.NORMAL + INVERT_COLOR + Back.BLUE + RIGHT_ARROW,
    print Fore.WHITE + Style.BRIGHT + virtualenv_name,

    INVERT_COLOR = Fore.BLUE

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

    OLD_INVERT_COLOR = INVERT_COLOR

    BACK_COLOR = Back.WHITE
    FORE_COLOR = Fore.BLACK
    INVERT_COLOR = Fore.WHITE
    STYLE = Style.DIM

    if needs_staging:
        BACK_COLOR = Back.RED
        FORE_COLOR = Fore.YELLOW
        INVERT_COLOR = Fore.RED
        STYLE = Style.BRIGHT
    elif needs_committing:
        BACK_COLOR = Back.GREEN
        FORE_COLOR = Fore.WHITE
        INVERT_COLOR = Fore.GREEN
        STYLE = Style.BRIGHT

    print (BACK_COLOR + OLD_INVERT_COLOR + Style.NORMAL + RIGHT_ARROW +
           STYLE + FORE_COLOR),

    print branch_name.strip(),

print INVERT_COLOR + Back.RESET + Style.NORMAL + RIGHT_ARROW,

print Style.RESET_ALL

print Fore.GREEN + Style.BRIGHT + "$ " + Style.RESET_ALL,
