import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AL_Web",
    version="1.0.0",
    author="AdamantLife",
    author_email="",
    description="A collection of internet-usage code. Originally part of aclustoms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AdamantLife/al_web",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "bs4",
        "pillow",
        "requests",

        "al-decorators @ git+https://github.com/AdamantLife/AL_Decorators",
        ]
)
