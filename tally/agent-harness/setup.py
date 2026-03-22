from setuptools import setup
setup(
    name='cli-anything-tally',
    version='1.0.0',
    packages=['cli_anything.tally'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tally=cli_anything.tally:cli']},
)
