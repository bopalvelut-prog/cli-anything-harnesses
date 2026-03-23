from setuptools import setup
setup(
    name='cli-anything-amazon_polly',
    version='1.0.0',
    packages=['cli_anything.amazon_polly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_polly=cli_anything.amazon_polly:cli']},
)
