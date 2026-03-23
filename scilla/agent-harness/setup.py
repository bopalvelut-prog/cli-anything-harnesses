from setuptools import setup
setup(
    name='cli-anything-scilla',
    version='1.0.0',
    packages=['cli_anything.scilla'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scilla=cli_anything.scilla:cli']},
)
