import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="execspeed",
    version="0.0.8",
    author="Ivan O'Connor",
    author_email="ivanoconnor@hotmail.co.uk",
    description="Simple tool for finding average function execution time",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Astrochamp/speed",
    project_urls={
        "Bug Tracker": "https://github.com/Astrochamp/speed/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
