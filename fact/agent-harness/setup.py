from setuptools import setup
setup(
    name='cli-anything-fact',
    version='1.0.0',
    packages=['cli_anything.fact'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fact=cli_anything.fact:cli']},
)
