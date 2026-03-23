from setuptools import setup
setup(
    name='cli-anything-zswap',
    version='1.0.0',
    packages=['cli_anything.zswap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zswap=cli_anything.zswap:cli']},
)
