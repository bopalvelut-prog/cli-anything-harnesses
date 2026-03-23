from setuptools import setup
setup(
    name='cli-anything-interest',
    version='1.0.0',
    packages=['cli_anything.interest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-interest=cli_anything.interest:cli']},
)
