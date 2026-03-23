from setuptools import setup
setup(
    name='cli-anything-chain',
    version='1.0.0',
    packages=['cli_anything.chain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chain=cli_anything.chain:cli']},
)
