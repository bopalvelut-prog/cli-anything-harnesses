from setuptools import setup
setup(
    name='cli-anything-symbol',
    version='1.0.0',
    packages=['cli_anything.symbol'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-symbol=cli_anything.symbol:cli']},
)
