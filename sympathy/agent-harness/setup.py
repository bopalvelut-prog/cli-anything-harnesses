from setuptools import setup
setup(
    name='cli-anything-sympathy',
    version='1.0.0',
    packages=['cli_anything.sympathy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sympathy=cli_anything.sympathy:cli']},
)
