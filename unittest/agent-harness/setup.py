from setuptools import setup
setup(
    name='cli-anything-unittest',
    version='1.0.0',
    packages=['cli_anything.unittest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unittest=cli_anything.unittest:cli']},
)
