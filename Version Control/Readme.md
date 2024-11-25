# Version Control

_Version control, In general, refers to management of changes to document,computer program,large web sites, and other collection of information.Version control software keep track of every modification to the code or a content in a special kind of database._

## Git

_Git is a distributed version control system (DVCS) designed to handle everything from small to very large project with speed and efficiency. It allow multiple developer to collaborate on a project, tacking changes to file and coordinating their work seamlessly._

## GitHub

_Github is a web-based platform built around git.It provide hosting for git repositories and adds additional features like bug tracking, task management, and wikis for every project._

# Working

_When we create a repository our default branch is main.We can create many branches like dev for development or other for bug fixing and after that we merge our all code in master branch._

- _To check current branch_
  ```
  git branch
  ```
- _To make latest changes from main repository to local repository_
  ```
  git pull
  ```
  _If you are working with different branches_
  ```
  git pull origin <branch-name>
  ```
- _To create a new branch_
  ```
  git checkout -b <name>
  ```
- _To add changes in branch_
  ```
  git add .
  ```
- _To add message or note with changes_
  ```
  git commit -m "your-message"
  ```
- _To push changes into the branch_
  ```
  git push origin <your-branch-name>
  ```
- _To change the branch_
  ```
  git checkout <branch-name>
  ```
- _To delete the branch_
  ```
  git checkout -D <branch-name>
  ```
- _To check status_
  ```
  git status
  ```

# Merge vs Rebase

_Suppose we are working on two different branches. One is main and other is dev. On one event I want to merge these two branches. When we merge this, it will create a new commit. After that we will start our work with updated data. The advantage is that we have history of that commit.The disadvantage is that when we review this its hard to understand where the data coming from before the commit._

_In rebase we basically move our dev branch to the head of the main branch.Also all the commit will convert into new commit.The advantage is the its easy to review the branch but disadvantage is the we have no longer history of that because all of the branch moved to the head of the main branch._

**Rule**

_Never use rebase to a public repository._

## Advance Commands

- _To check log_
  ```
  git log
  ```
- _To move commit from one branch to another_

  ```
  git cherry-pick <commit-hash>
  ```

  - _Note: You can get hash of your commit using git log command._

- _To reset you branch_
  ```
  git reset --hard origin/<branch-name>
  ```
  - _Note: This will remove all the data which is not commit._
