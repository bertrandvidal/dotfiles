dotfiles
========

All those files you spend hours customizing and just don't want to lose!

Install
=======

Paste the whole block into Terminal. The first line lets zsh treat the `#` lines
as comments; without it, zsh tries to run them as commands.

```sh
setopt interactive_comments
# Xcode Command Line Tools (git, python3, compilers): if missing, open the installer and wait until it's done
xcode-select -p >/dev/null 2>&1 || { xcode-select --install; until xcode-select -p >/dev/null 2>&1; do sleep 5; done; } && \
    # Homebrew: run the official installer unless /opt/homebrew/bin/brew already exists
    { [ -x /opt/homebrew/bin/brew ] || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"; } && \
    # Put brew on the PATH for the rest of this command (zprofile does it for new shells)
    eval "$(/opt/homebrew/bin/brew shellenv)" && \
    # Command-line tools: git, python3, pyenv, GitHub CLI, mise, direnv
    brew install git python pyenv gh mise direnv && \
    # ~/.ssh folder, readable only by you
    mkdir -p -m 700 ~/.ssh && \
    # SSH key: create ~/.ssh/id_ed25519 only if it doesn't exist yet; asks for a passphrase
    { [ -f ~/.ssh/id_ed25519 ] || ssh-keygen -t ed25519 -C "$(whoami)@$(scutil --get LocalHostName)" -f ~/.ssh/id_ed25519; } && \
    # Load the key into the ssh agent and save its passphrase in the macOS Keychain (asked once)
    ssh-add --apple-use-keychain ~/.ssh/id_ed25519 && \
    # Log in to GitHub in the browser; it offers to upload ~/.ssh/id_ed25519.pub to your account
    gh auth login --hostname github.com --git-protocol ssh --web && \
    # Trust GitHub's SSH host keys, fetched from its API over HTTPS, unless they're already known
    { ssh-keygen -F github.com >/dev/null 2>&1 || gh api meta --jq '.ssh_keys[] | "github.com " + .' >> ~/.ssh/known_hosts; } && \
    # oh-my-zsh: --unattended stops it from opening a nested zsh that pauses this command ("" fills sh -c's $0)
    sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended && \
    # powerlevel10k prompt theme, cloned into oh-my-zsh's custom themes folder
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k && \
    # Folder that holds the dotfiles clone
    mkdir -p ~/github && \
    # Clone the dotfiles over SSH, using the key set up above
    git clone git@github.com:bertrandvidal/dotfiles.git ~/github/dotfiles && \
    # Symlink every file listed in config.json into your home folder (existing files are backed up first)
    ~/github/dotfiles/install.py && \
    # Vundle, the plugin manager ~/.vimrc uses
    git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim && \
    # Install the plugins listed in ~/.vimrc; quit vim with :qa once it's done
    vim -c PluginInstall &&
    # Mac apps: MonitorControl, Bluesnooze, Rectangle
    brew install --cask MonitorControl bluesnooze rectangle && \
    # Every pending macOS update, Command Line Tools included; asks for your password
    sudo softwareupdate --install -a && \
    # Prompt setup wizard, only if ~/.p10k.zsh doesn't exist; runs in a new zsh, where p10k is loaded
    { [ -f ~/.p10k.zsh ] || zsh -i -c 'p10k configure'; }
```
