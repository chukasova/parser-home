import os
from setuptools import setup, find_packages

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_version():
    path = os.path.join(BASE_DIR, "VERSION")
    with open(path, "r") as version_file:
        return version_file.read().strip()


VERSION = get_version()


def get_license_file():
    return os.path.join(BASE_DIR, "LICENSE")


def get_long_description():
    path = os.path.join(BASE_DIR, "README.md")
    with open(path, "r") as readme_file:
        return readme_file.read().strip()


def get_requires():
    path = os.path.join(BASE_DIR, "requirements.txt")
    with open(path, "r") as require_file:
        packages = [
            package.strip() for package in require_file.read().strip().split("\n")
        ]
    return packages


ARGS = {
    "name": "parser",
    "version": VERSION,
    "author": "TMS",
    "author_email": "dmitriy.amelchenko@bpmobile.com",
    "url": "",
    "packages": find_packages("src", exclude=["*test*"]),
    "package_dir": {"": "src"},
    # "test_suite": "tests",
    "include_package_data": True,
    "license": get_license_file(),
    "description": "News parser",
    "long_description": get_long_description(),
    "long_description_content_type": "text/markdown",
    "install_requires": get_requires(),
    "python_requires": ">=3.8",
    "zip_safe": False,
    # "entry_points": {"console_scripts": ["parser = parser.app.main"]},
    "classifiers": [
        "Development Status :: 3 - Alpha"
        if "dev" in VERSION
        else "Development Status :: 4 - Beta"
        if "rc" in VERSION
        else "Development Status :: 5 Production/Stable"
    ],
}

setup(**ARGS)
