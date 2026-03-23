from setuptools import setup
setup(
    name='cli-anything-simple',
    version='1.0.0',
    packages=['cli_anything.simple'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-simple=cli_anything.simple:cli']},
)
