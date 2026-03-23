from setuptools import setup
setup(
    name='cli-anything-zig',
    version='1.0.0',
    packages=['cli_anything.zig'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zig=cli_anything.zig:cli']},
)
