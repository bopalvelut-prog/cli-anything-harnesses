from setuptools import setup
setup(
    name='cli-anything-acrolinx',
    version='1.0.0',
    packages=['cli_anything.acrolinx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-acrolinx=cli_anything.acrolinx:cli']},
)
