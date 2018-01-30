#!/bin/bash

BEGIN_PATTERN="---BEGIN-MY-OWN-ADDITIONS---"
END_PATTERN="---END-MY-OWN-ADDITIONS---"

ALIASES=".bash_aliases"
PROFILE=".profile"
BASHRC=".bashrc"

write_prefix() {
  printf '#' >> $1
  echo $BEGIN_PATTERN >> $1
}

write_postfix() {
  printf '#' >> $1
  echo $END_PATTERN >> $1
}

remove_additions() {
  sed -i.bak "/$BEGIN_PATTERN/,/$END_PATTERN/d" $1
  rm $1.bak
}

install_file() {
  [ ! -f $HOME/$1 ] && touch $HOME/$1
  remove_additions $HOME/$1
  write_prefix $HOME/$1
  cat $1 >> $HOME/$1
  write_postfix $HOME/$1
}

case "$(uname)" in
   Darwin*) install_file $PROFILE && install_file $BASHRC && install_file $ALIASES ;;
   Linux*)  install_file $BASHRC && install_file $ALIASES ;;
   *)       install_file $BASHRC && install_file $ALIASES ;;
esac

# Platform independent
cp .vimrc $HOME/.vimrc
cp .gitconfig $HOME/.gitconfig
