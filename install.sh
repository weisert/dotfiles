#!/bin/bash

if [ ! -f ~/.bash_aliases ]; then
    cp .bash_aliases ~/.bash_aliases
    echo $'export PATH=$PATH:~/.bin\n' >> ~/.bashrc
fi

