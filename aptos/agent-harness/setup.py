from setuptools import setup
setup(
    name='cli-anything-aptos',
    version='1.0.0',
    packages=['cli_anything.aptos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aptos=cli_anything.aptos:cli']},
)
