from setuptools import setup
setup(
    name='cli-anything-amazon_snowball',
    version='1.0.0',
    packages=['cli_anything.amazon_snowball'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_snowball=cli_anything.amazon_snowball:cli']},
)
