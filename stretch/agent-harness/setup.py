from setuptools import setup
setup(
    name='cli-anything-stretch',
    version='1.0.0',
    packages=['cli_anything.stretch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stretch=cli_anything.stretch:cli']},
)
