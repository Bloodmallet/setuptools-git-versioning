# setuptools-git-versioning

[![PyPI version](https://badge.fury.io/py/setuptools-git-versioning.svg)](https://badge.fury.io/py/setuptools-git-versioning)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/setuptools-git-versioning)](https://badge.fury.io/py/setuptools-git-versioning)
[![Build Status](https://github.com/dolfinus/setuptools-git-versioning/workflows/Tests/badge.svg)](https://github.com/dolfinus/setuptools-git-versioning/actions)
[![codecov](https://codecov.io/gh/dolfinus/setuptools-git-versioning/branch/master/graph/badge.svg?token=GIMVHUTNW4)](https://codecov.io/gh/dolfinus/setuptools-git-versioning)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/dolfinus/setuptools-git-versioning/master.svg)](https://results.pre-commit.ci/latest/github/dolfinus/setuptools-git-versioning/master)

Use git repo data (latest tag, current commit hash, etc) for building a version number according [PEP-440](https://www.python.org/dev/peps/pep-0440/).

## Comparing with other packages

| Package/Function                                                                                    | Latest release |    License    |     Python2 support      | Python3 support | Windows support | PEP 440 compatible | Type hints | Way of configuration | Supported substitutions                              | Dev template support | Dirty template support | Initial version support | Callback/variable as current version | Read some file content as current version | Write discovered version to a file | Development releases (prereleases) support | Reusing functions in other packages | Tests |
| --------------------------------------------------------------------------------------------------- | -------------: | :-----------: | :----------------------: | :-------------: | :-------------: | :----------------: | :--------: | :------------------: | ---------------------------------------------------- | :------------------: | :--------------------: | :---------------------: | :----------------------------------: | :---------------------------------------: | :--------------------------------: | :----------------------------------------: | :---------------------------------: | :---: |
| [setuptools-git-versioning](https://github.com/dolfinus/setuptools-git-versioning)                  |           2021 |      MIT      |            +             |      3.5+       |        +        |         +          |     +      |  setup.py/setup.cfg  | tag, commits_count, short_sha, full_sha, branch, env, timestamp |          +           |           +            |            +            |                  +                   |                     +                     |                 -                  |                     +                      |                  +                  |   +   |
| [setuptools-scm](https://github.com/pypa/setuptools_scm)                                            |           2021 |      MIT      | removed in 6.0.0 release |      3.6+       |        +        |         +          |     +      |    pyproject.toml    | tag, commits_count, short_sha, timestamp                        |          +           |           +            |            +            |                  -                   |                     -                     |                 +                  |                     +                      |                  +                  |   +   |
| [versioneer](https://github.com/python-versioneer/python-versioneer)                                |           2020 | Public Domain |            -             |      3.6+       |        +        |         +          |     -      |      setup.cfg       | tag, commits_count, short_sha, full_sha, timestamp              |          +           |           +            |            -            |                  -                   |                     +                     |                 +                  |                     +                      |                  +                  |   +   |
| [setuptools-git-ver](https://github.com/camas/setuptools-git-ver) (Base package)                    |           2019 |      MIT      |            -             |      3.7+       |        +        |         -          |     -      |  setup.py/setup.cfg  | tag, commits_count, short_sha                                   |          +           |           +            |            -            |                  -                   |                     -                     |                 -                  |                     -                      |                  -                  |   -   |
| [another-setuptools-git-version](https://github.com/ZdenekM/another-setuptools-git-version)         |           2020 |      MIT      |            -             |      3.5+       |        -        |         +          |     +      |  setup.py/setup.cfg  | tag, commits_count                                              |          +           |           -            |            +            |                  -                   |                     -                     |                 -                  |                     -                      |                  +                  |   -   |
| [bad-setuptools-git-version](https://github.com/st7105/bad-setuptools-git-version)                  |           2020 |      MIT      |            +             |        +        |        +        |         +          |     -      |  setup.py/setup.cfg  | tag, commits_count                                             |          +           |           -            |            +            |                  -                   |                     -                     |                 -                  |                     -                      |                  +                  |   -   |
| [even-better-setuptools-git-version](https://github.com/ktemkin/even-better-setuptools-git-version) |           2019 |      MIT      |            -             |        +        |        -        |         +          |     -      |  setup.py/setup.cfg  | tag, short_sha                                                 |          -           |           -            |            +            |                  -                   |                     -                     |                 -                  |                     -                      |                  +                  |   -   |
| [better-setuptools-git-version](https://github.com/vivin/better-setuptools-git-version)             |           2018 |      MIT      |            -             |        +        |        -        |         -          |     -      |  setup.py/setup.cfg  | tag, short_sha                                                 |          -           |           -            |            +            |                  -                   |                     -                     |                 -                  |                     -                      |                  +                  |   -   |
| [very-good-setuptools-git-version](https://github.com/Kautenja/very-good-setuptools-git-version)    |           2018 |      MIT      |            -             |        +        |        -        |         -          |     -      |  setup.py/setup.cfg  | tag, commits_count, short_sha                                  |          -           |           -            |            -            |                  -                   |                     -                     |                 -                  |                     -                      |                  +                  |   -   |
| [setuptools-git-version](https://github.com/pyfidelity/setuptools-git-version)                      |           2018 |    Unknown    |            +             |        +        |        +        |         -          |     -      |  setup.py/setup.cfg  | tag, commits_count, short_sha                                  |          -           |           -            |            -            |                  -                   |                     -                     |                 -                  |                     -                      |                  -                  |  -/+  |

## Installation

No need.

Adding `setup_requires=['setuptools-git-versioning']` somewhere in `setup.py` will automatically download the latest version from PyPi and save it in the `.eggs` folder when `setup.py` is run.

## Usage
### pyproject.toml
Just add this line into your `pyproject.toml`:

```toml
[tool.setuptools_git_versioning]
```

### setup.py
Just add these lines into your `setup.py`:

```python
setuptools.setup(version_config=True, setup_requires=["setuptools-git-versioning"], ...)
```

### Release version = git tag

You want to use git tag as a release number instead of duplicating it setup.py or other file.

For example, current repo state is:

```bash
commit 86269212 Release commit (HEAD, master)
|
commit e7bdbe51 Another commit
|
...
|
commit 273c47eb Long long ago
|
...
```

Then you decided to release new version:
- Tag commit with a proper release version (e.g. `v1.0.0` or `1.0.0`):

    ```bash
    commit 86269212 Release commit (v1.0.0, HEAD, master)
    |
    commit e7bdbe51 Another commit
    |
    ...
    |
    commit 273c47eb Long long ago
    |
    ...
    ```

- Check current version with command `python setup.py --version`.
- You'll get `1.0.0` as a version number. If tag number had `v` prefix, like `v1.0.0`, it will be trimmed.

#### Version number template

By default, when you try to get current version, you'll receive version number like `1.0.0`.

You can change this template just in the same `setup.py` file:

```python
setuptools.setup(
    version_config={
        "template": "2021.{tag}",
    },
    setup_requires=["setuptools-git-versioning"],
    ...,
)
```

In this case, for tag `3.4` version number will be `2021.3.4`

#### Dev template

For example, current repo state is:

```bash
commit 86269212 Current commit (HEAD, master)
|
commit 86269212 Release commit (v1.0.0)
|
commit e7bdbe51 Another commit
|
...
|
commit 273c47eb Long long ago
|
...
```

By default, when you try to get current version, you'll receive version number like `1.0.0.post1+git.64e68cd`.

This is a PEP-440 compliant value, but sometimes you want see just `1.0.0.post1` value or even `1.0.0`.

You can change this template just in the same `setup.py` file:

- For values like `1.0.0.post1`. `N` in `.postN` suffix is a number of commits since previous release (tag):

    ```python
    setuptools.setup(
        version_config={
            "dev_template": "{tag}.dev{ccount}",
        },
        setup_requires=["setuptools-git-versioning"],
        ...,
    )
    ```

- To return just the latest tag value, like `1.0.0`,use these options:

    ```python
    version_config = {
        "dev_template": "{tag}",
    }
    ```

#### Dirty template

For example, current repo state is:

```bash
Unstashed changes (HEAD)
|
commit 86269212 Current commit (master)
|
commit 86269212 Release commit (v1.0.0)
|
commit e7bdbe51 Another commit
|
...
|
commit 273c47eb Long long ago
|
...
```

By default, when you try to get current version, you'll receive version number like `1.0.0.post1+git.64e68cd.dirty`.
This is a PEP-440 compliant value, but sometimes you want see just `1.0.0.post1` value or even `1.0.0`.

You can change this template just in the same `setup.py` file:

- For values like `1.0.0.post1`. `N` in `.postN` suffix is a number of commits since previous release (tag):

    ```python
    setuptools.setup(
        version_config={
            "dirty_template": "{tag}.dev{ccount}",
        },
        setup_requires=["setuptools-git-versioning"],
        ...,
    )
    ```

- To return just the latest tag value, like `1.0.0`,use these options:

    ```python
    version_config = {
        "dirty_template": "{tag}",
    }
    ```

#### Set initial version

For example, current repo state is:

```bash
commit 86269212 Current commit (HEAD, master)
|
commit e7bdbe51 Another commit
|
...
|
commit 273c47eb Long long ago
|
...
```

And there are just no tags in the current branch.

By default, when you try to get current version, you'll receive some initial value, like `0.0.1`

You can change this template just in the same `setup.py` file:

```python
setuptools.setup(
    version_config={
        "starting_version": "1.0.0",
    },
    setup_requires=["setuptools-git-versioning"],
    ...,
)
```

### Callback/variable as current version

For example, current repo state is:

```bash
commit 233f6d72 Dev branch commit (HEAD, dev)
|
|    commit 86269212 Current commit (v1.0.0, master)
|    |
|   commit e7bdbe51 Another commit
|    /
...
|
commit 273c47eb Long long ago
|
...
```

And there are just no tags in the current branch (`dev`) because all of them are placed in the `master` branch only.

By default, when you try to get current version, you'll receive some initial value. But if you want to get synchronized version numbers in both on the branches?

You can create a function in some file (for example, in the `__init__.py` file of your module):

```python
def get_version():
    return "1.0.0"
```

Then place it in both the branches and update your `setup.py` file:

```python
from mymodule import get_version

setuptools.setup(
    version_config={
        "version_callback": get_version,
    },
    setup_requires=["setuptools-git-versioning"],
    ...,
)
```

When you'll try to get current version in non-master branch, the result of executing this function will be returned instead of latest tag number.

If a value of this option is not a function but just str, it also could be used:

- `__init__.py` file:

    ```python
    __version__ = "1.0.0"
    ```

- `setup.py` file:

    ```python
    from mymodule import __version__

    setuptools.setup(
        version_config={
            "version_callback": __version__,
        },
        setup_requires=["setuptools-git-versioning"],
        ...,
    )
    ```

**Please take into account that `version_callback` is ignored if tag is present**

### Read some file content as current version
Just like the previous example, but instead you can save current version in a simple test file instead of `.py` script.

Just create a file (for example, `VERSION` or `VERSION.txt`) and place here a version number:

```txt
1.0.0
```

Then place it in both the branches and update your `setup.py` file:

```python
import os

HERE = os.path.dirname(__file__)
VERSION_FILE = os.path.join(HERE, "VERSION")

setuptools.setup(
    version_config={
        "version_file": VERSION_FILE,
    },
    setup_requires=["setuptools-git-versioning"],
    ...,
)
```

When you'll try to get current version in non-master branch, the content of this file will be returned instead.

### Development releases (prereleases) from `dev` branch

For example, current repo state is:

```bash
commit 233f6d72 Dev branch commit (HEAD, dev)
|
|    commit 86269212 Current commit (v1.0.0, master)
|    |
|   commit e7bdbe51 Another commit
|    /
...
|
commit 273c47eb Long long ago
|
...
```

You want to make development releases (prereleases) from commits to a `dev` branch.
But there are just no tags here because all of them are placed in the `master` branch only.

Just like the examples above, create a file with a release number (e.g. `1.1.0`) in the `dev` branch, e.g. `VERSION.txt`:

```txt
1.1.0
```

But place here **next release number** instead of current one.

Then update your `setup.py` file:

```python
import os

HERE = os.path.dirname(__file__)
VERSION_FILE = os.path.join(HERE, "VERSION.txt")

setuptools.setup(
    version_config={
        "count_commits_from_version_file": True,
        "dev_template": "{tag}.dev{ccount}",  # suffix now is not .post, but .dev
        "dirty_template": "{tag}.dev{ccount}",  # same thing here
        "version_file": VERSION_FILE,
    },
    setup_requires=["setuptools-git-versioning"],
    ...,
)
```

Then you decided to release new version:

- Merge `dev` branch into `master` branch.
- Tag commit in the `master` branch with a proper release version (e.g. `v1.1.0`). Tag will be used as a version number for the release.
- Save next release version (e.g. `1.2.0`) in `VERSION` or `version.py` file in the `dev` branch. **Do not place any tags in the `dev` branch!**
- Next commits to a `dev` branch will lead to returning this next release version plus dev suffix, like `1.1.0.dev1` or so.
- `N` in `.devN` suffix is a number of commits since the last change of a certain file.
- **Note: every change of this file in the `dev` branch will lead to this `N` suffix to be reset to `0`. Update this file only in the case when you've setting up the next release version!**

### Development releases (prereleases) from any branch (`feature`/`bugfix`/`preview`/`beta`/etc)

Just like previous example, but you want to make development releases (prereleases) with a branch name present in the version number.

In case of branch names which are PEP-440 compatible, you can just use `{branch}` substitution in a version template.

For example, if the branch name is something like `alpha`, `beta`, `preview` or `rc`:

```python
setuptools.setup(
    version_config={
        "count_commits_from_version_file": True,
        "dev_template": "{tag}.{branch}{ccount}",
        "dirty_template": "{tag}.{branch}{ccount}",
        "version_file": VERSION_FILE,
    },
    setup_requires=["setuptools-git-versioning"],
    ...,
)
```

Adding a commit to the `alpha` branch will generate a version number like `1.2.3a4`, new commit to the `beta` branch will generate a version number like `1.2.3b5` and so on.

It is also possible to use branch names prefixed with a major version number, like `1.0-alpha` or `1.1.beta`:

```python
setuptools.setup(
    version_config={
        "count_commits_from_version_file": True,
        "dev_template": "{branch}{ccount}",
        "dirty_template": "{branch}{ccount}",
        "version_file": VERSION_FILE,
    },
    setup_requires=["setuptools-git-versioning"],
    ...,
)
```

Adding a commit to the `1.0-alpha` branch will generate a version number like `1.0a2`, new commit to the `1.2.beta` branch will generate a version number like `1.2b3` and so on.

But if branch name is not PEP-440 compatible at all, like `feature/ABC-123` or `bugfix/ABC-123`, you'll get version number which `pip` cannot understand.

To fix that you can define a callback which will receive current branch name and return a properly formatted one:

```python
import re


def format_branch_name(name):
    # If branch has name like "bugfix/issue-1234-bug-title", take only "1234" part
    pattern = re.compile("^(bugfix|feature)\/issue-([0-9]+)-\S+")

    match = pattern.search(name)
    if not match:
        return match.group(2)

    # function is called even if branch name is not used in a current template
    # just left properly named branches intact
    if name == "master":
        return name

    # fail in case of wrong branch names like "bugfix/issue-title"
    raise ValueError(f"Wrong branch name: {name}")


setuptools.setup(
    version_config={
        "dev_template": "{branch}.dev{ccount}",
        "dirty_template": "{branch}.dev{ccount}",
        "branch_formatter": format_branch_name,
    },
    setup_requires=["setuptools-git-versioning"],
    ...,
)
```

## Options

Default options are:

```toml
# pyproject.toml
[build-system]
requires = [
    "setuptools>=45",
    "wheel",
    "setuptools-git-versioning",
]
build-backend = "setuptools.build_meta"

[tool.setuptools_git_versioning]
template = "{tag}"
dev_template = "{tag}.post{ccount}+git.{sha}"
dirty_template = "{tag}.post{ccount}+git.{sha}.dirty"
starting_version = "0.0.1"
count_commits_from_version_file = false
```

```python
# setup.py
setuptools.setup(
    version_config={
        "template": "{tag}",
        "dev_template": "{tag}.post{ccount}+git.{sha}",
        "dirty_template": "{tag}.post{ccount}+git.{sha}.dirty",
        "starting_version": "0.0.1",
        "version_callback": None,
        "version_file": None,
        "count_commits_from_version_file": False,
        "branch_formatter": None,
        "sort_by": None,
    },
    setup_requires=["setuptools-git-versioning"],
    ...,
)
```

- `template`: used if no untracked files and latest commit is tagged

- `dev_template`: used if no untracked files and latest commit isn't tagged

- `dirty_template`: used if untracked files exist or uncommitted changes have been made

- `starting_version`: static value, used if not tags exist in repo

- `version_callback`: variable or callback function to get version instead of using `starting_version`

- `version_file`: path to VERSION file, to read version from it instead of using `static_version`

- `count_commits_from_version_file`: `True` to fetch `version_file` last commit instead of tag commit, `False` otherwise

- `branch_formatter`: callback to be used for formatting a branch name before template substitution

- `sort_by`: format string passed to ``git tag --sort=`` command to sort the output. Possible values: ``version:refname`` (alphanumeric sort), ``committerdate`` (commit date of tag), ``taggerdate`` (tag creation date), ``creatordate`` (either commit date or tag creation date, **default**). See [StackOverflow](https://stackoverflow.com/questions/67206124/what-is-the-difference-between-taggerdate-and-creatordate-for-git-tags) for more info.

    Note: please do not create annotated tags in the past,
    it can cause issues with detecting versions of existing commits.

### Substitutions

You can use these substitutions in `template`, `dev_template` or `dirty_template` options:

- `{tag}`: Latest tag in the repository

- `{ccount}`: Number of commits since last tag or last `version_file` commit (see `count_commits_from_version_file`)

- `{full_sha}`: Full sha hash of the latest commit

- `{sha}`: First 8 characters of the sha hash of the latest commit

- `{branch}`: Current branch name

- `{env:SOMEVAR}`: Value of environment variable `SOMEVAR`. Examples:

  - You can pass default value using `{env:SOMEVAR:default}` syntax.

  - Default value for missing variables is `UNKNOWN`. If you need to just skip the substitution, use `{env:SOMEVAR:IGNORE}` syntax.

  - It is possible to pass another substitution instead of a default value using `{env:SOMEVAR:{subst}}` syntax, e.g. `{env:BUILD_NUMBER:{ccount}}`.

- `{timestamp:format}`: Current timestamp rendered into a specified format. Examples:

  - `{timestamp}` or `{timestamp:%s}` will result `1632181549` (Unix timestamp).

  - `{timestamp:%Y-%m-%dT%H-%M-%S}` will result `2021-09-21T12:34:56`.

## Common issues

### Every version built by CI is `dirty`

This is usually caused by some files created by CI pipeline like build artifacts or test reports, e.g. `dist/my_package.whl` or `reports/unit.xml`.
If they are not mentioned in `.gitignore` file they will be recognized by git as untracked.
Because of that `git status` will report that you have uncommitted (dirty) changes in the index, so `setuptools-git-versioning` will detect current version as `dirty`.

You should such files to the `.gitignore` file. See [current repo `.gitignore`](https://github.com/dolfinus/setuptools-git-versioning/blob/master/.gitignore) as an example.
