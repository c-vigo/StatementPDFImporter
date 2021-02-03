# -*- coding: utf-8 -*-
# Author: Carlos Vigo
# Contact: carviher1990@gmail.com

from setuptools import setup

from os.path import join, dirname, abspath
from sys import path as sys_path
sys_path.append(abspath('pdf_importer'))
import __project__                        # noqa: E402


# Read the README.md file
with open(join(dirname(__file__), 'README.md'), "r") as fh:
    long_description = fh.read()

setup(
    name=__project__.__package_name__,
    version=__project__.__version__,
    author=__project__.__short_author__,
    author_email=__project__.__email__,
    description=__project__.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__project__.__url__,
    packages=['pdf_importer'],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    license='GPLv3',
    keywords=[
        'PDF'
    ],
    python_requires='>=3.6',
    setup_requires=[
        'pip>=10.0',
        'wheel',
        'setuptools>=30',
    ],
    install_requires=[
        'camelot-py',
        'python-dateutil',
        'opencv-python',
        'pandas'
    ],
    include_package_data=True
)
