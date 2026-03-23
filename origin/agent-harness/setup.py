from setuptools import setup
setup(
    name='cli-anything-origin',
    version='1.0.0',
    packages=['cli_anything.origin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-origin=cli_anything.origin:cli']},
)
