from setuptools import setup
setup(
    name='cli-anything-throat',
    version='1.0.0',
    packages=['cli_anything.throat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-throat=cli_anything.throat:cli']},
)
