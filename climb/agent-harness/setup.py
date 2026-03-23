from setuptools import setup
setup(
    name='cli-anything-climb',
    version='1.0.0',
    packages=['cli_anything.climb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-climb=cli_anything.climb:cli']},
)
