from setuptools import setup
setup(
    name='cli-anything-init',
    version='1.0.0',
    packages=['cli_anything.init'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-init=cli_anything.init:cli']},
)
