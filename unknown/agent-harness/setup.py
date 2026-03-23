from setuptools import setup
setup(
    name='cli-anything-unknown',
    version='1.0.0',
    packages=['cli_anything.unknown'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unknown=cli_anything.unknown:cli']},
)
