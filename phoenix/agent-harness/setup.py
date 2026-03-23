from setuptools import setup
setup(
    name='cli-anything-phoenix',
    version='1.0.0',
    packages=['cli_anything.phoenix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-phoenix=cli_anything.phoenix:cli']},
)
