from setuptools import setup
setup(
    name='cli-anything-cash',
    version='1.0.0',
    packages=['cli_anything.cash'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cash=cli_anything.cash:cli']},
)
