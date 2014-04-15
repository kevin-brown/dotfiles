# Ignore interactive

[[ "$-" != *i* ]] && return

# Ignore duplicates in the history

export HISTCONTROL=$HISTCONTROL${HISTCONTROL+,}ignoredups

# Better file listing, automatically include hidden files

alias ls="ls -la"

alias emacs="emacs -nw"

alias git=hub

# Load virtualenvwrapper if it is installed

if [ -e "/usr/bin/virtualenvwrapper.sh" ]; then
    source /usr/bin/virtualenvwrapper.sh
elif [ -e "/usr/local/bin/virtualenvwrapper.sh" ]; then
    source /usr/local/bin/virtualenvwrapper.sh
fi

if [ -e "/etc/bash_completion" ]; then
    source /etc/bash_completion
fi

shopt -s histverify

VIRTUAL_ENV_DISABLE_PROMPT=1
PS1='$(/usr/bin/python ~/.prompt.py)'
