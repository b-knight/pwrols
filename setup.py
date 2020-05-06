with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pwrols", 
    version="0.0.1",
    author="Benjamin S. Knight",
    author_email="knight.benjamin@gmail.com",
    description="Python package for sample size estimation in the context of OLS.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/b-knight/pwrols",
    install_requires=['scipy'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

