from setuptools import setup
setup(
    name='cli-anything-suspect',
    version='1.0.0',
    packages=['cli_anything.suspect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-suspect=cli_anything.suspect:cli']},
)
