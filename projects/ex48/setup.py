try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A project for Learn Python The Hard Way - Exercise 48',
    'author': 'Alex Liew',
    'url': '',
    'download_url': '',
    'author_email': 'alex.ljz@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'Project EX48'
}

setup(**config)
