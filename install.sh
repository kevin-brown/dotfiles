#!/bin/bash

files="bashrc gitconfig emacs prompt.py vimrc"

name=$(uname -s)

# Symlink the files to the home directory

for fileName in $files
do
    # Symlinks cannot be moved, so just remove them

    if [ -h "${HOME}/.${fileName}" ]
    then
        echo ".${fileName} is a symlink, removing it"
        rm "$HOME/.${fileName}"
    fi

    # Hard links and other files can be moved, so back them up

    if [ -e "${HOME}/.${fileName}" ]
    then
        echo ".${fileName} already exists, moving it to .${fileName}_old"
        mv "$HOME/.${fileName}" "$HOME/.${fileName}_old"
    fi

    ln -s "$PWD/.$fileName" "$HOME/.$fileName"
    echo "Created symlink .${fileName} <=====> $HOME/.$fileName"
done
