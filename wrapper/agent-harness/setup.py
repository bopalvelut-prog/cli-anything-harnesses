from setuptools import setup
setup(
    name='cli-anything-wrapper',
    version='1.0.0',
    packages=['cli_anything.wrapper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wrapper=cli_anything.wrapper:cli']},
)
