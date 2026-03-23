from setuptools import setup
setup(
    name='cli-anything-bats',
    version='1.0.0',
    packages=['cli_anything.bats'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bats=cli_anything.bats:cli']},
)
