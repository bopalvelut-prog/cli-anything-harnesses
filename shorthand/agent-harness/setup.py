from setuptools import setup
setup(
    name='cli-anything-shorthand',
    version='1.0.0',
    packages=['cli_anything.shorthand'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shorthand=cli_anything.shorthand:cli']},
)
