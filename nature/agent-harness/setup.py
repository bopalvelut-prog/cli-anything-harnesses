from setuptools import setup
setup(
    name='cli-anything-nature',
    version='1.0.0',
    packages=['cli_anything.nature'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nature=cli_anything.nature:cli']},
)
