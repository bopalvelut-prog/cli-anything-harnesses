from setuptools import setup
setup(
    name='cli-anything-initial',
    version='1.0.0',
    packages=['cli_anything.initial'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-initial=cli_anything.initial:cli']},
)
