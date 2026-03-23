from setuptools import setup
setup(
    name='cli-anything-east',
    version='1.0.0',
    packages=['cli_anything.east'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-east=cli_anything.east:cli']},
)
