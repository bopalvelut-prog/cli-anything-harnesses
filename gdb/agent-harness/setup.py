from setuptools import setup
setup(
    name='cli-anything-gdb',
    version='1.0.0',
    packages=['cli_anything.gdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gdb=cli_anything.gdb:cli']},
)
