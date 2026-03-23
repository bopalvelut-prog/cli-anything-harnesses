from setuptools import setup
setup(
    name='cli-anything-throw',
    version='1.0.0',
    packages=['cli_anything.throw'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-throw=cli_anything.throw:cli']},
)
