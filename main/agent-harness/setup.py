from setuptools import setup
setup(
    name='cli-anything-main',
    version='1.0.0',
    packages=['cli_anything.main'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-main=cli_anything.main:cli']},
)
