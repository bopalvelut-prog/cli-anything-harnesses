from setuptools import setup
setup(
    name='cli-anything-ldaps',
    version='1.0.0',
    packages=['cli_anything.ldaps'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ldaps=cli_anything.ldaps:cli']},
)
