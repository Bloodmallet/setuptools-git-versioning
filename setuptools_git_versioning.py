import os
import subprocess

from setuptools.dist import Distribution
from distutils.errors import DistutilsSetupError
from typing import List, Optional, Any

try:
    from collections.abs import Mapping
except ImportError:
    from collections import Mapping

DEFAULT_TEMPLATE = "{tag}"  # type: str
DEFAULT_DEV_TEMPLATE = "{tag}.dev{ccount}+git.{sha}"  # type: str
DEFAULT_DIRTY_TEMPLATE = "{tag}.dev{ccount}+git.{sha}.dirty"  # type: str


def _exec(cmd):  # type: (str) -> List[str]
    try:
        stdout = subprocess.check_output(cmd, shell=True,
                                         universal_newlines=True)
    except subprocess.CalledProcessError as e:
        stdout = e.output
    lines = stdout.splitlines()
    return [line.rstrip() for line in lines if line.rstrip()]


def get_tags():  # type: () -> List[str]
    tags = _exec("git tag --sort=-version:refname --merged")
    if tags:
        return tags
    return []


def get_tag():  # type: () -> Optional[str]
    tags = get_tags()
    if tags:
        return tags[0]
    return None


def get_sha(name):  # type: (str) -> Optional[str]
    sha = _exec("git rev-list -n 1 {name}".format(name=name))
    if sha:
        return sha[0]
    return None


def is_dirty():  # type: () -> bool
    res = _exec("git status --short")
    if res:
        return True
    return False


def count_since(name):  # type: (str) -> Optional[int]
    res = _exec("git rev-list --count HEAD ^{name}".format(name=name))
    if res:
        return int(res[0])
    return None


def parse_config(dist, _, value):  # type: (Distribution, Any, Any) -> None
    if isinstance(value, bool):
        if value:
            version = version_from_git()
            dist.metadata.version = version
            return
        else:
            raise DistutilsSetupError("Can't be False")

    if not isinstance(value, Mapping):
        raise DistutilsSetupError("Config in the wrong format")

    template = value['template'] if 'template' in value else DEFAULT_TEMPLATE
    dev_template = value['dev_template'] if 'dev_template' in value \
        else DEFAULT_DEV_TEMPLATE
    dirty_template = value['dirty_template'] if 'dirty_template' in value \
        else DEFAULT_DIRTY_TEMPLATE

    version = version_from_git(
        template=template,
        dev_template=dev_template,
        dirty_template=dirty_template,
    )
    dist.metadata.version = version


def version_from_git(template=DEFAULT_TEMPLATE,
                     dev_template=DEFAULT_DEV_TEMPLATE,
                     dirty_template=DEFAULT_DIRTY_TEMPLATE,
                     ):  # type: (str, str, str) -> None

    # Check if PKG-INFO exists and return value in that if it does
    if os.path.exists('PKG-INFO'):
        with open('PKG-INFO', 'r') as f:
            lines = f.readlines()
        for line in lines:
            if line.startswith('Version:'):
                return line[8:].strip()

    tag = get_tag()
    if tag is None:
        raise Exception("Couldn't find tag to use.")

    dirty = is_dirty()
    tag_sha = get_sha(tag)
    head_sha = get_sha('HEAD')
    ccount = count_since(tag)
    on_tag = head_sha == tag_sha

    if dirty:
        t = dirty_template
    elif not on_tag:
        t = dev_template
    else:
        t = template

    return t.format(sha=head_sha[:8], tag=tag, ccount=ccount)