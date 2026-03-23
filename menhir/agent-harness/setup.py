from setuptools import setup
setup(
    name='cli-anything-menhir',
    version='1.0.0',
    packages=['cli_anything.menhir'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-menhir=cli_anything.menhir:cli']},
)
