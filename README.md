dotfiles
========

All those files you spend hours customizing and just don't want to lose!

Install
=======

```sh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && \
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k && \
    mkdir ~/github && \
    git clone git@github.com:bertrandvidal/dotfiles.git ~/github/dotfiles && \
    python ~/github/dotfiles/install.py && \
    git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim && \
    vim -c PluginInstall
```
