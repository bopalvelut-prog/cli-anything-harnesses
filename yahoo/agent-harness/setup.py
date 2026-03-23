from setuptools import setup
setup(
    name='cli-anything-yahoo',
    version='1.0.0',
    packages=['cli_anything.yahoo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yahoo=cli_anything.yahoo:cli']},
)
