from setuptools import setup
setup(
    name='cli-anything-chocolatey',
    version='1.0.0',
    packages=['cli_anything.chocolatey'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chocolatey=cli_anything.chocolatey:cli']},
)
