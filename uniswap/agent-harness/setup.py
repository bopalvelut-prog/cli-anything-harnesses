from setuptools import setup
setup(
    name='cli-anything-uniswap',
    version='1.0.0',
    packages=['cli_anything.uniswap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-uniswap=cli_anything.uniswap:cli']},
)
