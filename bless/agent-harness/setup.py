from setuptools import setup
setup(
    name='cli-anything-bless',
    version='1.0.0',
    packages=['cli_anything.bless'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bless=cli_anything.bless:cli']},
)
