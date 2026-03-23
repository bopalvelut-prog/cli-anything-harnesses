from setuptools import setup
setup(
    name='cli-anything-amazon_ivs',
    version='1.0.0',
    packages=['cli_anything.amazon_ivs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_ivs=cli_anything.amazon_ivs:cli']},
)
