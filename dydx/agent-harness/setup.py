from setuptools import setup
setup(
    name='cli-anything-dydx',
    version='1.0.0',
    packages=['cli_anything.dydx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dydx=cli_anything.dydx:cli']},
)
