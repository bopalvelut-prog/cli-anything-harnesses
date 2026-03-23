from setuptools import setup
setup(
    name='cli-anything-basket',
    version='1.0.0',
    packages=['cli_anything.basket'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-basket=cli_anything.basket:cli']},
)
