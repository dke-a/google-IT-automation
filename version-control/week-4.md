# Collaboration

## Pull Requests

When collaborating on projects hosted on Github: 

1. Create a fork of repo
2. Work on forked repo
3. Create pull request

`Pull request` A commit or series of commits that are sent to owner of repo to incorporate into their tree.

### Typical Pull Request Workflow on Github

1. Fork repo
2. Clone repo from own account
   * `git clone <repo location>`
3. Create branch
   * `git checkout -b <branch name>`

### Squashing Changes

Should not rewrite history when commits have been published. However, this is waived with pull requests since it is only you who have cloned your fork of the repo.

`rebase -i <branch>`create a single commit that includes both changes and a more detailed descrpition.

Text editor opens with a list of all selected commits from oldest to most recent.

