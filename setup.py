from setuptools import setup

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

    py_modules=['visplt'],
    
    install_requires=requires,
)
