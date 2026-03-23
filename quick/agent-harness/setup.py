from setuptools import setup
setup(
    name='cli-anything-quick',
    version='1.0.0',
    packages=['cli_anything.quick'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quick=cli_anything.quick:cli']},
)
