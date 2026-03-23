from setuptools import setup
setup(
    name='cli-anything-ops',
    version='1.0.0',
    packages=['cli_anything.ops'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ops=cli_anything.ops:cli']},
)
