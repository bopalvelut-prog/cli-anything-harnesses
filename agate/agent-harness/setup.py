from setuptools import setup
setup(
    name='cli-anything-agate',
    version='1.0.0',
    packages=['cli_anything.agate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-agate=cli_anything.agate:cli']},
)
