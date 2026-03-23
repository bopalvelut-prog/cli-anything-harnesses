from setuptools import setup
setup(
    name='cli-anything-gdb_v2',
    version='1.0.0',
    packages=['cli_anything.gdb_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gdb_v2=cli_anything.gdb_v2:cli']},
)
