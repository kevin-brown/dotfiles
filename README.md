Dotfiles
========
A set of dotfiles that work for me.

Installation
------------
All you need to do install these dotfiles is install git and run this
command in whatever directory you store your projects in.

```
git clone https://github.com/kevin-brown/dotfiles.git dotfiles
cd dotfiles
source bootstrap.sh
```

Please change your information in `.gitconfig`, I don't want random commits
made under my name.

Making changes
--------------
This is meant to be flexible, but any changes you make will be overriden on
the next update from GitHub.  Any old copies of the files are backed up when
you run the script, so it shouldn't be too difficult to reset any changes.
Git also handles this with merging, so it might not be much of an issue.

All files are symlinked from where you cloned the repository, so it is easy
to update them if you really feel like it.

Feedback
--------
Found an issue?  Think I should add something?  [I'm open to suggestions.](https://github.com/kevin-brown/dotfiles/issues)
