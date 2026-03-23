from setuptools import setup
setup(
    name='cli-anything-organic',
    version='1.0.0',
    packages=['cli_anything.organic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-organic=cli_anything.organic:cli']},
)
