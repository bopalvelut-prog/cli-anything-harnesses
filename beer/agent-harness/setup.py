from setuptools import setup
setup(
    name='cli-anything-beer',
    version='1.0.0',
    packages=['cli_anything.beer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-beer=cli_anything.beer:cli']},
)
