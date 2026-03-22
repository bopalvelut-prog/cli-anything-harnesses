from setuptools import setup
setup(
    name='cli-anything-bzz',
    version='1.0.0',
    packages=['cli_anything.bzz'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bzz=cli_anything.bzz:cli']},
)
