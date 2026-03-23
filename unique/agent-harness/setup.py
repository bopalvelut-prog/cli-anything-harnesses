from setuptools import setup
setup(
    name='cli-anything-unique',
    version='1.0.0',
    packages=['cli_anything.unique'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unique=cli_anything.unique:cli']},
)
