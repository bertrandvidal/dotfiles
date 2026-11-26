dotfiles
========

All those files you spend hours customizing and just don't want to lose!

Install
=======

```sh
xcode-select -p >/dev/null 2>&1 || { xcode-select --install; until xcode-select -p >/dev/null 2>&1; do sleep 5; done; } && \
    { [ -x /opt/homebrew/bin/brew ] || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"; } && \
    eval "$(/opt/homebrew/bin/brew shellenv)" && \
    brew install git python pyenv gh && \
    mkdir -p -m 700 ~/.ssh && \
    { [ -f ~/.ssh/id_ed25519 ] || ssh-keygen -t ed25519 -C "$(whoami)@$(scutil --get LocalHostName)" -f ~/.ssh/id_ed25519; } && \
    ssh-add --apple-use-keychain ~/.ssh/id_ed25519 && \
    gh auth login --hostname github.com --git-protocol ssh --web && \
    { ssh-keygen -F github.com >/dev/null 2>&1 || gh api meta --jq '.ssh_keys[] | "github.com " + .' >> ~/.ssh/known_hosts; } && \
    sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended && \
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k && \
    mkdir -p ~/github && \
    git clone git@github.com:bertrandvidal/dotfiles.git ~/github/dotfiles && \
    ~/github/dotfiles/install.py && \
    git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim && \
    vim -c PluginInstall &&
    brew install mise direnv &&
    brew install --cask MonitorControl bluesnooze rectangle && \
    sudo softwareupdate --install -a && \
    { [ -f ~/.p10k.zsh ] || zsh -i -c 'p10k configure'; }
```
