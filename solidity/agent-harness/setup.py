from setuptools import setup
setup(
    name='cli-anything-solidity',
    version='1.0.0',
    packages=['cli_anything.solidity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-solidity=cli_anything.solidity:cli']},
)
