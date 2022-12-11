dotfiles
========

All those files you spend hours customizing and you just don't want to lose them

Install
=======

```sh
mkdir ~/github && \
  git clone git@github.com:bertrandvidal/dotfiles.git ~/github/dotfiles && \
   python ~/github/dotfiles/install.py && \
   git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim && \
   vim -c PluginInstall
```
