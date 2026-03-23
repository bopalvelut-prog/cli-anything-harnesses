from setuptools import setup
setup(
    name='cli-anything-plutus',
    version='1.0.0',
    packages=['cli_anything.plutus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plutus=cli_anything.plutus:cli']},
)
