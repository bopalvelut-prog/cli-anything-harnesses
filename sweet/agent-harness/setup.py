from setuptools import setup
setup(
    name='cli-anything-sweet',
    version='1.0.0',
    packages=['cli_anything.sweet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sweet=cli_anything.sweet:cli']},
)
