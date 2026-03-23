from setuptools import setup
setup(
    name='cli-anything-symphony',
    version='1.0.0',
    packages=['cli_anything.symphony'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-symphony=cli_anything.symphony:cli']},
)
