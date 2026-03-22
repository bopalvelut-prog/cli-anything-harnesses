from setuptools import setup
setup(
    name='cli-anything-ida',
    version='1.0.0',
    packages=['cli_anything.ida'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ida=cli_anything.ida:cli']},
)
