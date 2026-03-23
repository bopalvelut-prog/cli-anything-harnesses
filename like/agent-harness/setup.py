from setuptools import setup
setup(
    name='cli-anything-like',
    version='1.0.0',
    packages=['cli_anything.like'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-like=cli_anything.like:cli']},
)
