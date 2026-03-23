from setuptools import setup
setup(
    name='cli-anything-authelia',
    version='1.0.0',
    packages=['cli_anything.authelia'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-authelia=cli_anything.authelia:cli']},
)
