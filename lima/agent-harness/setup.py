from setuptools import setup
setup(
    name='cli-anything-lima',
    version='1.0.0',
    packages=['cli_anything.lima'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lima=cli_anything.lima:cli']},
)
