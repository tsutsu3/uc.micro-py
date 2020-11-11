import re
from os import path

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(path.join(path.dirname(__file__), "uc_micro", "__init__.py")) as f:
    match = re.search(r"__version__\s*=\s*[\'\"](.+?)[\'\"]", f.read())
    version = match.group(1)

setuptools.setup(
    name="uc-micro-py",
    version=version,
    license="MIT",
    author="tsutsu3",
    description="Micro subset of unicode data files for linkify-it-py projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tsutsu3/uc.micro-py",
    packages=setuptools.find_packages(exclude=["test"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    keywords="unicode",
    extras_require={
        "test": [
            "coverage",
            "pytest",
            "pytest-cov",
        ]
    },
)
