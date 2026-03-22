from setuptools import setup
setup(
    name='cli-anything-pancakeswap',
    version='1.0.0',
    packages=['cli_anything.pancakeswap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pancakeswap=cli_anything.pancakeswap:cli']},
)
