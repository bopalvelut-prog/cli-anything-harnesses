from setuptools import setup
setup(
    name='cli-anything-lion',
    version='1.0.0',
    packages=['cli_anything.lion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lion=cli_anything.lion:cli']},
)
