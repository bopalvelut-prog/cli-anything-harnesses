from setuptools import setup
setup(
    name='cli-anything-instead',
    version='1.0.0',
    packages=['cli_anything.instead'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-instead=cli_anything.instead:cli']},
)
