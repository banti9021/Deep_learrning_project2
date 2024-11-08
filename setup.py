#(2)
import setuptools
from setuptools import find_packages
import os

# Attempt to read the README file, providing a fallback if it does not exist
try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "A small python package for CNN app."  # Fallback description

__version__ = "0.0.0"

REPO_NAME = "Deep_learrning_project2"
AUTHOR_USER_NAME = "banti9021"
SRC_REPO = "deep_learning"
AUTHOR_EMAIL = "nbanti943@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
)
