from setuptools import setup
setup(
    name='cli-anything-shelf',
    version='1.0.0',
    packages=['cli_anything.shelf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shelf=cli_anything.shelf:cli']},
)
