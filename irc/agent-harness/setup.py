from setuptools import setup
setup(
    name='cli-anything-irc',
    version='1.0.0',
    packages=['cli_anything.irc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-irc=cli_anything.irc:cli']},
)
