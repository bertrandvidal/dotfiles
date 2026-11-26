dotfiles
========

All those files you spend hours customizing and just don't want to lose!

Install
=======

```sh
xcode-select -p >/dev/null 2>&1 || { xcode-select --install; until xcode-select -p >/dev/null 2>&1; do sleep 5; done; } && \
    sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && \
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k && \
    mkdir ~/github && \
    git clone git@github.com:bertrandvidal/dotfiles.git ~/github/dotfiles && \
    ~/github/dotfiles/install.py && \
    git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim && \
    vim -c PluginInstall &&
    brew install mise direnv gh &&
    brew install --cask MonitorControl bluesnooze rectangle && \
    sudo softwareupdate --install -a
```

Update
======

The Xcode Command Line Tools are updated through Software Update, along with
macOS itself:

```sh
sudo softwareupdate --install -a
```
