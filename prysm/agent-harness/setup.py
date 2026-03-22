from setuptools import setup
setup(
    name='cli-anything-prysm',
    version='1.0.0',
    packages=['cli_anything.prysm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prysm=cli_anything.prysm:cli']},
)
