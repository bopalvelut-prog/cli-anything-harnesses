from setuptools import setup
setup(
    name='cli-anything-infura',
    version='1.0.0',
    packages=['cli_anything.infura'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-infura=cli_anything.infura:cli']},
)
