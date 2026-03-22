from setuptools import setup
setup(
    name='cli-anything-sushiswap',
    version='1.0.0',
    packages=['cli_anything.sushiswap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sushiswap=cli_anything.sushiswap:cli']},
)
