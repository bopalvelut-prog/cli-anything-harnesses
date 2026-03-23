from setuptools import setup
setup(
    name='cli-anything-amazon_aurora',
    version='1.0.0',
    packages=['cli_anything.amazon_aurora'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_aurora=cli_anything.amazon_aurora:cli']},
)
