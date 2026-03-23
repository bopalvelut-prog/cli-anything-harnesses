from setuptools import setup
setup(
    name='cli-anything-wine',
    version='1.0.0',
    packages=['cli_anything.wine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wine=cli_anything.wine:cli']},
)
