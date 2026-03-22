from setuptools import setup
setup(
    name='cli-anything-starknet',
    version='1.0.0',
    packages=['cli_anything.starknet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-starknet=cli_anything.starknet:cli']},
)
