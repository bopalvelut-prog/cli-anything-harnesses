from setuptools import setup
setup(
    name='cli-anything-amazon_chime',
    version='1.0.0',
    packages=['cli_anything.amazon_chime'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_chime=cli_anything.amazon_chime:cli']},
)
