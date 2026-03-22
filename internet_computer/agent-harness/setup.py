from setuptools import setup
setup(
    name='cli-anything-internet_computer',
    version='1.0.0',
    packages=['cli_anything.internet_computer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-internet_computer=cli_anything.internet_computer:cli']},
)
