from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, "README.md")) as f:
    long_description = f.read()

setup(
    name="run-js",
    packages=["js"],
    package_dir={"js": "js"},
    package_data={"js": ["js/__init__.py", "js/exists.js", "js/run.js"]},
    version="0.0.2",
    description="Goal: The Easiest Way to Run JavaScript in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Daniel J. Dufour",
    author_email="daniel.j.dufour@gmail.com",
    url="https://github.com/DanielJDufour/run-js",
    download_url="https://github.com/DanielJDufour/run-js/tarball/download",
    keywords=[
        "functional",
        "javascript",
        "python",
        "package",
        "library",
        "universal",
        "python3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)
