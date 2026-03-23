from setuptools import setup
setup(
    name='cli-anything-leveldb',
    version='1.0.0',
    packages=['cli_anything.leveldb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-leveldb=cli_anything.leveldb:cli']},
)
