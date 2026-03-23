from setuptools import setup
setup(
    name='cli-anything-edition',
    version='1.0.0',
    packages=['cli_anything.edition'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-edition=cli_anything.edition:cli']},
)
