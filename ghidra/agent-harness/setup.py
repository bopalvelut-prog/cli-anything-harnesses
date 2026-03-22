from setuptools import setup
setup(
    name='cli-anything-ghidra',
    version='1.0.0',
    packages=['cli_anything.ghidra'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ghidra=cli_anything.ghidra:cli']},
)
