from setuptools import setup
setup(
    name='cli-anything-huginn',
    version='1.0.0',
    packages=['cli_anything.huginn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-huginn=cli_anything.huginn:cli']},
)
