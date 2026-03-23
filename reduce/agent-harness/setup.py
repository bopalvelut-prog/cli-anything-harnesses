from setuptools import setup
setup(
    name='cli-anything-reduce',
    version='1.0.0',
    packages=['cli_anything.reduce'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reduce=cli_anything.reduce:cli']},
)
