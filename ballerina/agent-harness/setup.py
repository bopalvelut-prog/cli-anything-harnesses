from setuptools import setup
setup(
    name='cli-anything-ballerina',
    version='1.0.0',
    packages=['cli_anything.ballerina'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ballerina=cli_anything.ballerina:cli']},
)
