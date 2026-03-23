from setuptools import setup
setup(
    name='cli-anything-brew',
    version='1.0.0',
    packages=['cli_anything.brew'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-brew=cli_anything.brew:cli']},
)
