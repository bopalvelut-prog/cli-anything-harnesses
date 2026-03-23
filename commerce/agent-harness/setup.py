from setuptools import setup
setup(
    name='cli-anything-commerce',
    version='1.0.0',
    packages=['cli_anything.commerce'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-commerce=cli_anything.commerce:cli']},
)
