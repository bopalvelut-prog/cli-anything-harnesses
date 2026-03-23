from setuptools import setup
setup(
    name='cli-anything-nosql',
    version='1.0.0',
    packages=['cli_anything.nosql'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nosql=cli_anything.nosql:cli']},
)
