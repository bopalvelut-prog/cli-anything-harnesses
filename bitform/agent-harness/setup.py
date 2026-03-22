from setuptools import setup
setup(
    name='cli-anything-bitform',
    version='1.0.0',
    packages=['cli_anything.bitform'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bitform=cli_anything.bitform:cli']},
)
