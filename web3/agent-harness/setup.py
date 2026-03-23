from setuptools import setup
setup(
    name='cli-anything-web3',
    version='1.0.0',
    packages=['cli_anything.web3'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-web3=cli_anything.web3:cli']},
)
