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

```sh
# working at CrowdTwist/Oracle
docker cp ~/.ssh/id_rsa web:/root/.ssh && \
docker cp ~/.ssh/id_rsa.pub web:/root/.ssh && \
docker exec -ti web mkdir /root/github && \
docker exec -ti web git clone git@github.com:bertrandvidal/dotfiles.git /root/github/dotfiles && \
docker exec -ti web python /root/github/dotfiles/install.py && \
docker exec -ti web git clone https://github.com/gmarik/Vundle.vim.git /root/.vim/bundle/Vundle.vim && \
docker exec -ti web vim -c PluginInstall && \
docker cp ~/github/dotfiles/git/prepare-commit-msg web:/opt/crowdtwist/.git/hooks/ && \
docker exec -ti web passwd
```

On a \*nix machine
```sh
sudo apt-get install git ipython keychain vim && \
  ssh-keygen -t dsa (generate a new ssh key, add it to github)
```

ToDo
====

* Add the concept of profile so I can have my personal/pro dotfiles
