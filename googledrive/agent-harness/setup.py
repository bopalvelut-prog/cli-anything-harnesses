from setuptools import setup
setup(
    name='cli-anything-googledrive',
    version='1.0.0',
    packages=['cli_anything.googledrive'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-googledrive=cli_anything.googledrive:cli']},
)
