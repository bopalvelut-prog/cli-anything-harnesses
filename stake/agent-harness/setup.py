from setuptools import setup
setup(
    name='cli-anything-stake',
    version='1.0.0',
    packages=['cli_anything.stake'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stake=cli_anything.stake:cli']},
)
