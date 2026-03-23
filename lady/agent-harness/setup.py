from setuptools import setup
setup(
    name='cli-anything-lady',
    version='1.0.0',
    packages=['cli_anything.lady'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lady=cli_anything.lady:cli']},
)
