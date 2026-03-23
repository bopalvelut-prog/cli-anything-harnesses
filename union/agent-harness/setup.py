from setuptools import setup
setup(
    name='cli-anything-union',
    version='1.0.0',
    packages=['cli_anything.union'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-union=cli_anything.union:cli']},
)
