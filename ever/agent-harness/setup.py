from setuptools import setup
setup(
    name='cli-anything-ever',
    version='1.0.0',
    packages=['cli_anything.ever'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ever=cli_anything.ever:cli']},
)
