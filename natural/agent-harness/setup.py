from setuptools import setup
setup(
    name='cli-anything-natural',
    version='1.0.0',
    packages=['cli_anything.natural'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-natural=cli_anything.natural:cli']},
)
