from setuptools import setup
setup(
    name='cli-anything-west',
    version='1.0.0',
    packages=['cli_anything.west'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-west=cli_anything.west:cli']},
)
