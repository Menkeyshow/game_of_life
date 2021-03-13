from setuptools import setup
from setuptools import find_packages
import re
from os.path import abspath, dirname, join

setup(
    name="menkeyshow.conway",
    version='0.0.1a',
    author="Maximilian Birkenhagen",
    author_email="maximilian.birkenhagen@gmail.com",
    description="Python implementation of Conway's Game of Life",
    url="https://github.com/Menkeyshow/game_of_life",
    package_dir={"": "src"},
    packages=find_packages("src"),
    entry_points={
        'console_scripts': [
            'conway = run_game:run'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],

)