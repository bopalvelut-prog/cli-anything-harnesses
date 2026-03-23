from setuptools import setup
setup(
    name='cli-anything-flood',
    version='1.0.0',
    packages=['cli_anything.flood'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flood=cli_anything.flood:cli']},
)
