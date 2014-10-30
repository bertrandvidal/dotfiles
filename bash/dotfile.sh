
DOTFILE=~/dotfiles

# Change dir to dotfiles
function dotcd(){
  cd $DOTFILE > /dev/null
}

# Get the diff of the current changes
function dotdiff(){
  cd $DOTFILE > /dev/null
  git diff
  cd - > /dev/null
}

# Get dotfiles git status
function dotstatus(){
  cd $DOTFILE > /dev/null
  git status -s -b -unormal
  cd - > /dev/null
}

# Pull changes from the repo
function dotpull(){
  cd $DOTFILE > /dev/null
  git pull --rebase origin master && git fetch origin
  cd - > /dev/null
}

# Deploy all dotfiles after pulling
function dotdeploy(){
  dotpull
  cd $DOTFILE > /dev/null
  ./install.py
  # source the newly deployed bashrc
  srcbash
  cd - > /dev/null
}

# Quickly push changes to repo, all args are used as the commit message
function dotpush(){
  # source the potentially modified bashrc
  srcbash
  cd $DOTFILE > /dev/null
  commit_msg="Dirty commit"
  [ $# -ne 0 ] && commit_msg=$*
  git commit -a -m "$commit_msg" && git push origin master
  cd - > /dev/null
}

