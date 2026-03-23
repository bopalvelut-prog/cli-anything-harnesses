from setuptools import setup
setup(
    name='cli-anything-colossus',
    version='1.0.0',
    packages=['cli_anything.colossus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-colossus=cli_anything.colossus:cli']},
)
