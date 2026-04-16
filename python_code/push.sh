# A

git push -u origin master

#B

# 1. 新建并切换到新分支（把 dev 改成你想要的名字，比如 feature/login） ^-^    Create and switch to a new branch (change dev to the name you want, such as feature/login)
git checkout -b xsm_666

# 2. 推送到远程 GitHub，并建立关联
git push -u origin xsm_666


# in xsm_666 merge master

git fetch
git merge origin/xsm_666


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