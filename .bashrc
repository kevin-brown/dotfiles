# Ignore interactive

[[ "$-" != *i* ]] && return

# Ignore duplicates in the history

export HISTCONTROL=$HISTCONTROL${HISTCONTROL+,}ignoredups

# Create links using MS mklink function

mln_func ()
{
    cmd /c mklink $(cygpath -aw $3) $(cygpath -aw $2)
}

# Better file listing, automatically include hidden files

alias ls="ls -la"
alias mln=mln_func

# Load virtualenvwrapper if it is installed

if [ -e "/usr/bin/virtualenvwrapper.sh" ]; then
    source /usr/bin/virtualenvwrapper.sh
elif [ -e "/usr/local/bin/virtualenvwrapper.sh" ]; then
    source /usr/local/bin/virtualenvwrapper.sh
fi

if [ -e "/etc/bash_completion" ]; then
    source /etc/bash_completion
fi
