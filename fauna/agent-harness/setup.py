from setuptools import setup
setup(
    name='cli-anything-fauna',
    version='1.0.0',
    packages=['cli_anything.fauna'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fauna=cli_anything.fauna:cli']},
)
