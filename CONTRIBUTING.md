# Guidelines for Contributing

Thank you for taking the time to contribute back to the project! Contributions in any form(e.g. issues, pull requests) are always welcomed by the development team. Please take some time to read through the following sections for guidelines on how to make your contribution as effective as possible.

## Issues

Issues can be used to report unexpected behavior in the project, ask general question, or make feature suggestions. Before opening a new issue, please adhere to the following guidelines.

* If you haven't already, please pull down and test against the latest version of the code.
* Before opening an issue, please check the current list of [open issues](https://github.com/Raznic/bailiwick/issues)and [closed issues](https://github.com/Raznic/bailiwick/issues?q=is%3Aissue+is%3Aclosed) to ensure that a similar issue hasn't already been reported.
* Open a [new issue](https://github.com/Raznic/bailiwick/issues/new) and provide all of the required information.

## Pull Requests

* Search the current list of [open issues](https://github.com/Raznic/bailiwick/issues) to check that no other developers are currently working on a similar change.
* If an issue does not already exist for the change, please create a [new issue](https://github.com/Raznic/bailiwick/issues/new). The issue will become the location where proposed changes can be discussed and tracked.
* Fork the repository. Please be sure to read the [development philosophy](#development-philosophy)to ensure your PR follows the standards for commits, branching, etc.
* Run tests locally to ensure there are no failures.
* Open the PR against the `master` branch.

## Development Philosophy

### 

This project uses a [trunk based development](https://trunkbaseddevelopment.com/) approach
(or a reasonable approximation there of). Developers should strive to make small changes with their updates. Small changes are favorable for a number of reasons:

* Easy to review.
* Can be merged into trunk branch (i.e. master) more often than large changes.

### Commit Messages

Commit messages should include the following:

* Title line summarizing the changes introduced by the commit.
* Body section (separated from title by a blank line) that goes into detail about the changes included in the commit. It should focus on explaining on what/why the change is being made, rather than the how.
* Optionally, it may include a footer (separated the body by a blank line) that includes the GitHub issues that it closes.
* Commit messages should follow the 50/72 rule. The first line (title) should not exceed 50 characters. All other lines in the message should not exceed 72 characters.

### Branching

Any new development work should be done on a separate branch. Branches should strive to be short-lived and only contain small, incremental changes. Avoiding long-running feature branches has several benefits:

* Easier to review.
* Can be merged into `master` more frequently.
* Avoids merge conflicts.

Branches should have an appropriate name. There is no strict naming scheme for branches, but it should be easy to tell at a glance what changes they contain. The following list contains examples of useful information to include in a branch name:

* Feature being developed
* GitHub issue number
* Type of work (e.g. feature, bugfix)
