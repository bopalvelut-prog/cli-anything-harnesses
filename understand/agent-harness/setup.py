from setuptools import setup
setup(
    name='cli-anything-understand',
    version='1.0.0',
    packages=['cli_anything.understand'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-understand=cli_anything.understand:cli']},
)
