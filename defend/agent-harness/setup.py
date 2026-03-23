from setuptools import setup
setup(
    name='cli-anything-defend',
    version='1.0.0',
    packages=['cli_anything.defend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-defend=cli_anything.defend:cli']},
)
