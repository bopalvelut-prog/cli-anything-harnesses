from setuptools import setup
setup(
    name='cli-anything-asgard',
    version='1.0.0',
    packages=['cli_anything.asgard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-asgard=cli_anything.asgard:cli']},
)
