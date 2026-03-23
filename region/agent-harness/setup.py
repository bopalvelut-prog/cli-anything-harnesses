from setuptools import setup
setup(
    name='cli-anything-region',
    version='1.0.0',
    packages=['cli_anything.region'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-region=cli_anything.region:cli']},
)
