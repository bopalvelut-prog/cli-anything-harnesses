from setuptools import setup
setup(
    name='cli-anything-yugabyte',
    version='1.0.0',
    packages=['cli_anything.yugabyte'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yugabyte=cli_anything.yugabyte:cli']},
)
