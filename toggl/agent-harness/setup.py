from setuptools import setup
setup(
    name='cli-anything-toggl',
    version='1.0.0',
    packages=['cli_anything.toggl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-toggl=cli_anything.toggl:cli']},
)
