from setuptools import setup
setup(
    name='cli-anything-acorn',
    version='1.0.0',
    packages=['cli_anything.acorn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-acorn=cli_anything.acorn:cli']},
)
