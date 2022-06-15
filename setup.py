import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gym-record",
    version="0.0.2",
    author="gyuta",
    description="A recorder for open ai gym. you can easily add a text on the frame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gyuta/gym_recorder",
    project_urls={
        "Bug Tracker": "https://github.com/gyuta/gym_recorder/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "gym",
        "opencv-python",
    ],
    packages=["gym_recorder"],
)