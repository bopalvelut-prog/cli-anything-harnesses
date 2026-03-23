from setuptools import setup
setup(
    name='cli-anything-m1',
    version='1.0.0',
    packages=['cli_anything.m1'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-m1=cli_anything.m1:cli']},
)
