from setuptools import setup
setup(
    name='cli-anything-fluid',
    version='1.0.0',
    packages=['cli_anything.fluid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fluid=cli_anything.fluid:cli']},
)
