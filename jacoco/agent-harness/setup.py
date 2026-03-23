from setuptools import setup
setup(
    name='cli-anything-jacoco',
    version='1.0.0',
    packages=['cli_anything.jacoco'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jacoco=cli_anything.jacoco:cli']},
)
