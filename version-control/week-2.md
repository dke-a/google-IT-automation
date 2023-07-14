# Week 2

## Advanced Git Interaction

`git commit -a`

skip staging but works only for tracked files. best for truly small changes.

### Cheatsheet

| Command           | Explanation & Link                                                                      |
|-------------------|-----------------------------------------------------------------------------------------|
| git commit -a     | Stages files automatically                                                              |
| git log -p        | Produces patch text                                                                     |
| git show          | Shows various objects                                                                   |
| git diff          | Is similar to the Linux `diff` command, and can show the differences in various commits |
| git diff --staged | An alias to --cached, this will show all staged files compared to the named commit      |
| git add -p        | Allows a user to interactively review patches to add to the current commit              |
| git mv            | Similar to the Linux `mv` command, this moves a file                                    |
| git rm            | Similar to the Linux `rm` command, this deletes, or removes a file                      |

There are many useful git cheatsheets online as well. Please take some time to research and study a few, such as [this one](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)

.gitignore files are used to tell the git tool to intentionally ignore some files in a given Git repository. For example, this can be useful for configuration files or metadata files that a user may not want to check into the master branch. Check out more at [here](https://git-scm.com/docs/gitignore).

A few common examples of file patterns to exclude can be found 
[here](https://gist.github.com/octocat/9257657).

## Undoing Things

`git checkout` restores file to latest snapshot. can be used to revert changes to modified files.

`git reset` use to unstage files. `git reset HEAD <filename>`

`git commit --amend` takes whatever is in staging area and runs git commit workflow to overwrite latest commit. add the change first before running amend. 

* AVOID using on shared repository. Use only on local!

`git revert HEAD` creates commit that contains inverse of all changes in the bad commit. when we pass `HEAD` to the revert command, we tell git to rewind that current commit

`git show <commit id>` to display commit information

`git revert <commit id>` to revert to previous commit

### Git Revert Cheat Sheet

[git checkout](https://git-scm.com/docs/git-checkout) is effectively used to switch branches.

[git reset](https://git-scm.com/docs/git-reset#_examples) asically resets the repo, throwing away some changes. It’s somewhat difficult to understand, so reading the examples in the documentation may be a bit more useful.

There are some other useful articles online, which discuss more aggressive approaches to 
resetting the repo
.

[git commit --amend](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---amend) is used to make changes to commits after-the-fact, which can be useful for making notes about a given commit.

[git revert](https://git-scm.com/docs/git-revert) makes a new commit which effectively rolls back a previous commit. It’s a bit like an undo command.

There are a  [few ways](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things) you can rollback commits in Git.

There are some interesting considerations about how git object data is stored, such as the usage of sha-1. 

Feel free to read more here:

<https://en.wikipedia.org/wiki/SHA-1>

<https://github.blog/2017-03-20-sha-1-collision-detection-on-github-com/>

## Branching and Merging

`Branch` is a pointer to a particular commit. Represents an independent line of development.

Can be used to list, create, delete, and manipulate branches.

`git branch <name>` to create a new branch.

`git checkout <name of branch>` to switch to branch.

`git checkout -b <name>` create and switch to new branch.

`git branch -d <name>` delete branch. if there are changes that have not been made to master branch, git will warn.

`Merging` combine branched data and history together.

`git merge <name>` will merge into master.

Algorithms: fast-forward and 3 way merge. 3 way merge may result in conflict if edits were done in same parts of same files. fast-foward is straight forward merging bec of no commit overlap.

In case of conflict:

* `git status`
* open file and git will show conflict.
* resolve conflict
* add to stage and commit

| Command                   | Explanation & Link                                                                                            |
|---------------------------|---------------------------------------------------------------------------------------------------------------|
| git branch                | Used to manage branches                                                                                       |
| git branch <name>         | Creates the branch                                                                                            |
| git branch -d <name>      | Deletes the branch                                                                                            |
| git branch -D <name>      | Forcibly deletes the branch                                                                                   |
| git checkout <branch>     | Switches to a branch.                                                                                         |
| git checkout -b <branch>  | Creates a new branch and switches to it .                                                                     |
| git merge <branch>        | Merge joins branches together .                                                                               |
| git merge --abort         | If there are merge conflicts (meaning files are incompatible), --abort can be used to abort the merge action. |
| git log --graph --oneline | This shows a summarized view of the commit history for a repo .                                               |

---

# Lab

$$$$