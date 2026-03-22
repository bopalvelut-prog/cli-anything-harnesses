from setuptools import setup
setup(
    name='cli-anything-fantom',
    version='1.0.0',
    packages=['cli_anything.fantom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fantom=cli_anything.fantom:cli']},
)
