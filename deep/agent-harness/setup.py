from setuptools import setup
setup(
    name='cli-anything-deep',
    version='1.0.0',
    packages=['cli_anything.deep'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deep=cli_anything.deep:cli']},
)
