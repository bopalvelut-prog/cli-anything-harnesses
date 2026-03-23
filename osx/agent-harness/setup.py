from setuptools import setup
setup(
    name='cli-anything-osx',
    version='1.0.0',
    packages=['cli_anything.osx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-osx=cli_anything.osx:cli']},
)
