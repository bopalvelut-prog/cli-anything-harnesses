from setuptools import setup
setup(
    name='cli-anything-witness',
    version='1.0.0',
    packages=['cli_anything.witness'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-witness=cli_anything.witness:cli']},
)
