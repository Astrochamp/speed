import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="speed",
    version="0.1.0",
    description="Calculates average running time of a function",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Astrochamp/speed",
    author="Ivan O'Connor",
    author_email="ivanoconnor@hotmail.co.uk",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["speed"],
    include_package_data=True,
)
