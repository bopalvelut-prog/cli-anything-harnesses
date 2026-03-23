from setuptools import setup
setup(
    name='cli-anything-ubuntu',
    version='1.0.0',
    packages=['cli_anything.ubuntu'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ubuntu=cli_anything.ubuntu:cli']},
)
