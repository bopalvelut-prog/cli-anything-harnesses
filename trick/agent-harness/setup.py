from setuptools import setup
setup(
    name='cli-anything-trick',
    version='1.0.0',
    packages=['cli_anything.trick'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trick=cli_anything.trick:cli']},
)
