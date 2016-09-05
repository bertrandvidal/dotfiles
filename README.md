dotfiles
========

All those files you spend hours customizing and you just don't want to lose them

Install
=======

* sudo apt-get install awesome awesome-extra git ipython keychain vim
* ssh-keygen -t dsa (generate a new ssh key, add it to github)
* `mkdir ~/github && git clone git@github.com:bertrandvidal/dotfiles.git && cd dotfile && python install.py`
* pip install wakatime
* git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim (run :PluginInstall)
* git clone https://github.com/gjsheep/bash-wakatime.git ~/github/

ToDo
====

* Add the concept of profile so I can have my personal/pro dotfiles
