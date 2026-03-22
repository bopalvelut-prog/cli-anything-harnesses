from setuptools import setup
setup(
    name='cli-anything-hardhat',
    version='1.0.0',
    packages=['cli_anything.hardhat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hardhat=cli_anything.hardhat:cli']},
)
