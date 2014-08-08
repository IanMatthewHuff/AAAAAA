AAAAAA
======

Automated Abstract Art Assembly And Appreciation

Guiding Principals

1. Have Fun!
2. Focus On Learning
3. Big Goals

GIT BASICS
==========

pw: dc1
git remote -v (Show Remote Settings)
git status
git diff
git clone git@github.com:username/reponame.git (Clone from github)

Config:
git config --global user.name "Alvin Alexander"
git config --global user.email YOUR-EMAIL-ADDRESS
file in ~/.gitconfig

Add File:
touch README
git add README
git commit -m 'yada yada'

or skip staging

touch README
git commit -a -m 'yada yada'

Move File:
git mv README readme.txt

Push To Remote:
git push origin master
