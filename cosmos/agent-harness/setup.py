from setuptools import setup
setup(
    name='cli-anything-cosmos',
    version='1.0.0',
    packages=['cli_anything.cosmos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cosmos=cli_anything.cosmos:cli']},
)
