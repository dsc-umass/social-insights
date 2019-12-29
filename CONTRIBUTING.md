# Contributing to health-insights

## Things you will need

 * Linux, Mac OS X, or Windows.
 * git (used for source version control).
 * An ssh client (used to authenticate with GitHub).

## Getting the code and configuring your environment


 * Ensure all the dependencies described in the previous section are installed.
 * Fork `https://github.com/dsc-umass/health-insights` into your own GitHub account. If
   you already have a fork, and are now installing a development environment on
   a new machine, make sure you've updated your fork so that you don't use stale
   configuration options from long ago.
 * If you haven't configured your machine with an SSH key that's known to github, then
   follow [GitHub's directions](https://help.github.com/articles/generating-ssh-keys/)
   to generate an SSH key.
 * `git clone git@github.com:<your_name_here>/synergy.git`
 * `cd plugins`
 * `git remote add upstream git@github.com:rishabnayak/synergy.git` (So that you
   fetch from the master repository, not your clone, when running `git fetch`
   et al.)

## Contributing code

We gladly accept contributions via GitHub pull requests.

To start working on a patch:

 * `git fetch upstream`
 * `git checkout upstream/master -b <name_of_your_branch>`
 * Hack away.
 * `git commit -a -m "<your informative commit message>"`
 * `git push origin <name_of_your_branch>`

To send us a pull request:

* `git pull-request` (if you are using [Hub](http://github.com/github/hub/)) or
  go to `https://github.com/dsc-umass/health-insights` and click the
  "Compare & pull request" button

Please make sure all your checkins have detailed commit messages explaining the patch.

Plugins tests are run automatically on contributions using Github Actions. However, due to
cost constraints, pull requests from non-committers may not run all the tests
automatically.

Once you've gotten an LGTM from a project maintainer and once your PR has received
the green light from all our automated testing, wait for one the package maintainers
to merge the pull request and `pub submit` any affected packages.

### The review process

* This is a new process we are currently experimenting with, feedback on the process is welcomed at the Gitter contributors channel. *

Reviewing PRs often requires a non trivial amount of time. We prioritize issues, not PRs, so that we use our maintainers' time in the most impactful way. Non trivial PRs should have an associated issue that will be used for prioritization.

Newly opened PRs first go through initial triage which results in one of:
  * **Merging the PR** - if the PR can be quickly reviewed and looks good.
  * **Closing the PR** - if the PR maintainer decides that the PR should not be merged.
  * **Moving the PR to the backlog** - if the review requires non trivial effort and the issue isn't a priority; in this case the maintainer will:
    * Make sure that the PR has an associated issue labeled with "plugin".
    * Add the "backlog" label to the issue.
    * Leave a comment on the PR explaining that the review is not trivial and that the issue will be looked at according to priority order.
  * **Starting a non trivial review** - if the review requires non trivial effort and the issue is a priority; in this case the maintainer will:
    * Add the "in review" label to the issue.
    * Self assign the PR.

### The release process

We push releases manually. Generally every merged PR upgrades at least one
plugin's `pubspec.yaml`, so also needs to be published as a package release. The
Synergy maintainer most involved with the PR should be the person responsible
for publishing the package release. In cases where the PR is authored by a
Synergy maintainer, the publisher should probably be the author. In other cases
where the PR is from a contributor, it's up to the reviewing Flutter team member
to publish the release instead.

Some things to keep in mind before publishing the release:

- Has CI ran on the master commit and gone green? Even if CI shows as green on
  the PR it's still possible for it to fail on merge, for multiple reasons.
  There may have been some bug in the merge that introduced new failures. CI
  runs on PRs as it's configured on their branch state, and not on tip of tree.
  CI on PRs also only runs tests for packages that it detects have been directly
  changed, vs running on every single package on master.
- "Don't deploy on a Friday." Consider carefully whether or not it's worth
  immediately publishing an update before a stretch of time where you're going
  to be unavailable. There may be bugs with the release or questions about it
  from people that immediately adopt it, and uncovering and resolving those
  support issues will take more time if you're unavailable.
