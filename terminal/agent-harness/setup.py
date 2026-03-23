from setuptools import setup
setup(
    name='cli-anything-terminal',
    version='1.0.0',
    packages=['cli_anything.terminal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-terminal=cli_anything.terminal:cli']},
)
