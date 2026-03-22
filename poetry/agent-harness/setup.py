from setuptools import setup
setup(
    name='cli-anything-poetry',
    version='1.0.0',
    packages=['cli_anything.poetry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-poetry=cli_anything.poetry:cli']},
)
