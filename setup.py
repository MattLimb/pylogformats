import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyLogFormats", # Replace with your own username
    version="0.0.1",
    author="Matt Limb",
    author_email="matt.limb17@gmail.com",
    description="A collection of useful log formats for Python Loggers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)