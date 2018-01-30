#!/bin/bash

git config --global user.name "FirstName SecondName"
git config --global user.email "username@yandex-team.ru"

git config --global branch.master.rebase true
git config --global branch.master.remote origin
git config --global branch.master.merge master

git config --global branch.autosetuprebase always

git config --global color.diff auto
git config --global color.status auto
git config --global color.branch auto

git config --global core.fscache true
git config --global core.preloadindex true
git config --global core.longpaths true

