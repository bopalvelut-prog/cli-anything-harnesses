from setuptools import setup
setup(
    name='cli-anything-assignment',
    version='1.0.0',
    packages=['cli_anything.assignment'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-assignment=cli_anything.assignment:cli']},
)
