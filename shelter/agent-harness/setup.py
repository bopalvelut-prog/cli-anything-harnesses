from setuptools import setup
setup(
    name='cli-anything-shelter',
    version='1.0.0',
    packages=['cli_anything.shelter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shelter=cli_anything.shelter:cli']},
)
