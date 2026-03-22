from setuptools import setup
setup(
    name='cli-anything-chainlink',
    version='1.0.0',
    packages=['cli_anything.chainlink'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chainlink=cli_anything.chainlink:cli']},
)
