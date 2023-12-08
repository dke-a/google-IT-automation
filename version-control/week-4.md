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

![](images/20230719223301.png)

Default action is `pick` which takes commits and rebases against branch selected.

`sqaush` combine both commits and modify commit message

![](images/20230719224316.png)

![](images/20230719225227.png)

Check out the following link for more information:

<https://help.github.com/en/articles/about-pull-request-merges>

## Code Reviews

Going through someone else's code, docs, or config and checking that all makes sense and follows expected patterns.

Improve the project by ensuring content is high quality, style is consistent, reducing bugs.

### More Information on Code Reviews

Check out the following links for more information:

* <http://google.github.io/styleguide/>
* <https://help.github.com/en/articles/about-pull-request-reviews>
* <https://medium.com/osedea/the-perfect-code-review-process-845e6ba5c31>
* <https://smartbear.com/learn/code-review/what-is-code-review/>

## Managing Projects

### Managing Collaboration

* Collaborating with others using tools like GitHub is helpful, but coordination outside the platform is also necessary.
* Give colleagues a heads up about significant code refactors to avoid conflicts.
* Documentation is essential when working with a large group. Clear code, comments, and README files.
* Promptly review and respond to pull requests to avoid conflicts and keep contributors motivated.
* Understand changes you accept, as the original contributor might not maintain the code.
* Be selective with accepting patches; too many changes can make the project hard to manage, while rejecting all might discourage contributors.
* Style guides help maintain consistent code style; consider creating one for your project if you own it.
* Issue trackers are useful for coordinating tasks in active software projects.
* For communication, use appropriate channels like mailing lists, IRC, Slack, Telegram, depending on project needs.
* Learn what communication channels are used in projects you collaborate with.

### Continuous Integration

* Automated tests can help ensure code functionality, but humans may forget to run them regularly.
* Continuous Integration (CI) systems automate code testing after every commit or pull request.
* CI helps verify that changes will pass tests before merging them into the main codebase.
* Continuous Deployment (CD) means frequently deploying new code to avoid large updates and catch errors early.
* CI/CD is a broader system known as CICD, with tools like Jenkins, Travis, GitLab, etc.
* **Pipelines** specify the steps needed to achieve the desired outcome in CICD.
* Artifacts are files generated during the pipeline, e.g., compiled code or documentation.
* Manage secrets carefully to grant pipeline access to servers; avoid using the same entities for test and production servers.
* Make sure authorized entities for test servers are not the same for deployment to production servers
* Always have a plan to recover access in case pipeline gets compromised.
* Add a YAML configuration file to define the language and pipeline steps for the project.

<details>
<summary>Additional Tools </summary>

Check out the following links for more information:

* <https://arp242.net/diy.html>
* <https://help.github.com/en/articles/closing-issues-using-keywords>
* <https://help.github.com/en/articles/setting-guidelines-for-repository-contributors>
* <https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html>
* <https://stackify.com/what-is-cicd-whats-important-and-how-to-get-it-right/>
* <https://docs.travis-ci.com/user/tutorial/>
* <https://docs.travis-ci.com/user/build-stages/>

</details>
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