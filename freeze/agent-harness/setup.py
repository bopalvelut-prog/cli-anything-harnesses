from setuptools import setup
setup(
    name='cli-anything-freeze',
    version='1.0.0',
    packages=['cli_anything.freeze'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-freeze=cli_anything.freeze:cli']},
)
