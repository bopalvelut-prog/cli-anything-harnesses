from setuptools import setup
setup(
    name='cli-anything-amazon_macie',
    version='1.0.0',
    packages=['cli_anything.amazon_macie'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_macie=cli_anything.amazon_macie:cli']},
)
