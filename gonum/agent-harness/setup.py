from setuptools import setup
setup(
    name='cli-anything-gonum',
    version='1.0.0',
    packages=['cli_anything.gonum'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gonum=cli_anything.gonum:cli']},
)
