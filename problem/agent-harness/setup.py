from setuptools import setup
setup(
    name='cli-anything-problem',
    version='1.0.0',
    packages=['cli_anything.problem'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-problem=cli_anything.problem:cli']},
)
