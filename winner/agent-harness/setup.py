from setuptools import setup
setup(
    name='cli-anything-winner',
    version='1.0.0',
    packages=['cli_anything.winner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-winner=cli_anything.winner:cli']},
)
