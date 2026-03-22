from setuptools import setup
setup(
    name='cli-anything-bookstack',
    version='1.0.0',
    packages=['cli_anything.bookstack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bookstack=cli_anything.bookstack:cli']},
)
