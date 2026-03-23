from setuptools import setup
setup(
    name='cli-anything-syntax',
    version='1.0.0',
    packages=['cli_anything.syntax'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-syntax=cli_anything.syntax:cli']},
)
