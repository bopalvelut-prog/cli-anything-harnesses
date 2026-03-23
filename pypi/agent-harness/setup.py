from setuptools import setup
setup(
    name='cli-anything-pypi',
    version='1.0.0',
    packages=['cli_anything.pypi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pypi=cli_anything.pypi:cli']},
)
