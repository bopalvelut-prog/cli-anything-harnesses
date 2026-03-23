from setuptools import setup
setup(
    name='cli-anything-nine',
    version='1.0.0',
    packages=['cli_anything.nine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nine=cli_anything.nine:cli']},
)
