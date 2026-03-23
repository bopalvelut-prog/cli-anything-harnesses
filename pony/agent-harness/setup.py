from setuptools import setup
setup(
    name='cli-anything-pony',
    version='1.0.0',
    packages=['cli_anything.pony'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pony=cli_anything.pony:cli']},
)
