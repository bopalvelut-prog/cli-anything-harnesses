from setuptools import setup
setup(
    name='cli-anything-green',
    version='1.0.0',
    packages=['cli_anything.green'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-green=cli_anything.green:cli']},
)
