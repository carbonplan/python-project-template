#!/usr/bin/env python

"""The setup script"""
import pathlib

from setuptools import find_packages, setup

DESCRIPTION = "carbonplan python project template"
LONG_DESCRIPTION = pathlib.Path("README.md").read_text()
PYTHON_REQUIRES = ">=3.10"

with open("requirements.txt") as f:
    INSTALL_REQUIRES = f.read().strip().split("\n")


setup(
    name="carbonplan-project",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    maintainer="CarbonPlan",
    maintainer_email="hello@carbonplan.org",
    url="https://github.com/carbonplan/python-project-template",
    packages=find_packages(),
    include_package_data=True,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    license="MIT",
    keywords="carbon, data, climate",
    use_scm_version={"version_scheme": "post-release", "local_scheme": "dirty-tag"},
)
