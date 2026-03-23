from setuptools import setup
setup(
    name='cli-anything-class',
    version='1.0.0',
    packages=['cli_anything.class'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-class=cli_anything.class:cli']},
)
