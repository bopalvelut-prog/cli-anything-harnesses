from setuptools import setup
setup(
    name='cli-anything-nethogs',
    version='1.0.0',
    packages=['cli_anything.nethogs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nethogs=cli_anything.nethogs:cli']},
)
