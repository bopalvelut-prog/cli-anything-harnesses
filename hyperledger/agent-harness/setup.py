from setuptools import setup
setup(
    name='cli-anything-hyperledger',
    version='1.0.0',
    packages=['cli_anything.hyperledger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hyperledger=cli_anything.hyperledger:cli']},
)
