from setuptools import setup
setup(
    name='cli-anything-standardnotes',
    version='1.0.0',
    packages=['cli_anything.standardnotes'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-standardnotes=cli_anything.standardnotes:cli']},
)
