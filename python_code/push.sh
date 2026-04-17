E1
# A
git fetch
git pull
增删改查
git push -u origin master

# B
# 1. 新建并切换到新分支（把 dev 改成你想要的名字，比如 feature/login） ^-^    Create and switch to a new branch (change dev to the name you want, such as feature/login)
git checkout -b xsm_666/git checkout xsm_666(如果有该分支，直接切换)

# 2. 推送到远程 GitHub，并建立关联
git push -u origin xsm_666


E2
# in xsm_666 merge master

git fetch
git merge origin/xsm_666


E3
# 不小心删了.git目录

首先，重新init
然后，关联远程仓库(shimei0203,xsm_2026_new)
git remote add origin https://github.com/shimei0203/xsm_2026_new.git
也许报错
# git remote add origin https://github.com/shimei0203/xsm_2026_new.git
error: remote origin already exists.
那么就执行下面的2步
# git remote remove origin
# git remote add origin https://github.com/shimei0203/xsm_2026_new.git
git fetch origin
git checkout main




E4
一些报错信息
# git push -u origin master
To https://github.com/shimei0203/xsm_2026_new.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/shimei0203/xsm_2026_new.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

解决办法
git pull origin master --allow-unrelated-histories
（最好别用）如果足够安全的情况下，强推覆盖
git push -f -u origin master


E5

git branch  ^-^  1. 查看本地所有分支

git branch -d 分支名  ^-^  1. 删除本地分支（已合并）

git branch -D 分支名  ^-^  2. 强制删除本地分支（不管合没合并）



E6 

有时候master和分支会变成两条线
这时候想要合并，需要将merge
在分支上merge master内容
解决办法：加一句参数强制合并
git merge master --allow-unrelated-histories
看一下哪些文件冲突
git status
你会看到红色的 both added 文件，就是要处理的。
处理完add commit 然后push
git push --set-upstream origin xsm_666


最终变成origin/xsm_666
# git status
On branch xsm_666
Your branch is up to date with 'origin/xsm_666'.

nothing to commit, working tree clean