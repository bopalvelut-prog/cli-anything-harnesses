from setuptools import setup
setup(
    name='cli-anything-wall',
    version='1.0.0',
    packages=['cli_anything.wall'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wall=cli_anything.wall:cli']},
)
