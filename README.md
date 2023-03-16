<p align="left" >
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://carbonplan-assets.s3.amazonaws.com/monogram/light-small.png">
  <img alt="CarbonPlan monogram." height="48" src="https://carbonplan-assets.s3.amazonaws.com/monogram/dark-small.png">
</picture>
</p>

# python-project-template

A CarbonPlan template for a developing a Python project

[![CI](https://github.com/carbonplan/python-project-template/actions/workflows/main.yaml/badge.svg)](https://github.com/carbonplan/python-project-template/actions/workflows/main.yaml)
[![License](https://img.shields.io/github/license/carbonplan/python-project-template?style=flat)](https://github.com/carbonplan/python-project-template/blob/main/LICENSE)

This CarbonPlan repository contains a template for developing a python project. To start, click on the green [Use this template](https://github.com/carbonplan/python-project-template/generate) button in the top right. This will allow you to create a new project using this base template.

## Modifications

### Updating project name

`scripts` and `tests` contain filler .py files. Update/remove these with your project name.

### Updating workflows/main.yaml

In the workflows/main.yaml file, the pytest and docker sections of the github actions configuration are currently commented out. If you wish to add them, uncomment them.

### Updating requirements.txt

requirements.txt is currently empty. You can populate it with: `pip3 freeze > requirements.txt`

## license

All the code in this repository is [MIT](https://choosealicense.com/licenses/mit/) licensed, but we request that you please provide attribution if reusing any of our digital content (graphics, logo, articles, etc.).

## about us

CarbonPlan is a non-profit organization that uses data and science for climate action. We aim to improve the transparency and scientific integrity of climate solutions with open data and tools. Find out more at [carbonplan.org](https://carbonplan.org/) or get in touch by [opening an issue](https://github.com/carbonplan/python-project-template/issues/new) or [sending us an email](mailto:hello@carbonplan.org).
