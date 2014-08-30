try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A project for Learn Python The Hard Way - Exercise 47',
    'author': 'Alex Liew',
    'url': '',
    'download_url': '',
    'author_email': 'alex.ljz@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'Project EX47'
}

setup(**config)
