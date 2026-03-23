from setuptools import setup
setup(
    name='cli-anything-amazon_inspector',
    version='1.0.0',
    packages=['cli_anything.amazon_inspector'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_inspector=cli_anything.amazon_inspector:cli']},
)
