from setuptools import setup, find_packages

from visplt import __version__

requires = [
    'numpy',
    'vispy',
]

setup(
    name='visplt',
    version=__version__,

    url='https://https://github.com/mkkb/visplt',
    author='Kristian Borve',
    author_email='mkkb4987@hotmail.com',

    packages=find_packages(),
    
    install_requires=requires,
)
