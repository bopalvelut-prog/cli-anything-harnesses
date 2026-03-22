from setuptools import setup
setup(
    name='cli-anything-iota',
    version='1.0.0',
    packages=['cli_anything.iota'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-iota=cli_anything.iota:cli']},
)
