git.md  
git remote add origin https://github.com/jaassoon/{}.git  
git fetch  
git branch --set-upstream-to=origin/{} master  
#### to merge with remote
git pull  
#### push after merged
git push origin HEAD:{}  
git clone -b {} https://github.com/jaassoon/{}.git {}  
#### if cant push
check your token is expire or not.  

git  
git - Applying .pdf  
git - Can I get a list of files marked --assume-unchanged_ - Stack Overflow.pdf  
git - No _pull_ in git gui_.pdf  
git pull の時に_You asked me to pull ...pdf  
git ready » temporarily ignoring files.pdf  
Keeping a fork up to date.pdf  
rebase - Git refusing to merge unrelated histories - Stack Overflow.pdf  


#### list file history
git mergetool
git merge develop
git merge origin/develop

###### disable popup compress
git config --global gui.gcwarning false

git stash show -u
git stash list
git stash show stash@{0}
```
git log --name-only  
git log -2
gitk [filename]
```
git config core.autocrlf true

git diff h1 h2 --name-only
git diff h1 h2 -- conf/xxx.conf  
##### how to merge branchs
git pull origin xxx --allow-unrelated-histories  

##### to new project branch  list all branches
git branch -a  
git checkout -b new_branch  
git push origin your_new_branch  

##### delete branch
git push origin --delete xx  
git branch -d xxx  
git branch --unset-upstream  
git branch --set-upstream-to=origin/your_branch master  
git pull origin HEAD:your_branch --allow-unrelated-histories  
git pull --allow-unrelated-histories  


##### rename current branch and track the remote branch
git branch -m xxx  
git push --set-upstream origin xxx  


remote  
git init --bare  

git update-index --assume-unchanged common.php
---------------------------------------------
```
git init --bare
git clone
git push origin master
git remote set-url origin /path/to/your/repos  
```
### 1. Clone your fork:

    git clone git@github.com:YOUR-USERNAME/YOUR-FORKED-REPO.git

### 2. Add remote from original repository in your forked repository: 

    cd into/cloned/fork-repo
    git remote add upstream git://github.com/ORIGINAL-DEV-USERNAME/REPO-YOU-FORKED-FROM.git
    git fetch upstream
    
```shell
$ tar -zxf git-2.0.0.tar.gz
$ cd git-2.0.0
$ make configure
$ ./configure --prefix=/usr
$ make all doc info
$ sudo make install install-doc install-html install-info
```

git config --global credential.helper stores
