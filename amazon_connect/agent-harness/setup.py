from setuptools import setup
setup(
    name='cli-anything-amazon_connect',
    version='1.0.0',
    packages=['cli_anything.amazon_connect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_connect=cli_anything.amazon_connect:cli']},
)
