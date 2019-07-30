dotfiles
========

All those files you spend hours customizing and you just don't want to lose them

Install
=======

* sudo apt-get install awesome awesome-extra git ipython keychain vim
* ssh-keygen -t dsa (generate a new ssh key, add it to github)
* `mkdir ~/github && git clone git@github.com:bertrandvidal/dotfiles.git ~/github/dotfiles && cd ~/github/dotfiles && python install.py && git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim && vim -c PluginInstall`

ToDo
====

* Add the concept of profile so I can have my personal/pro dotfiles
