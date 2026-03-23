from setuptools import setup
setup(
    name='cli-anything-shelve',
    version='1.0.0',
    packages=['cli_anything.shelve'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shelve=cli_anything.shelve:cli']},
)
