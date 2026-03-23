from setuptools import setup
setup(
    name='cli-anything-align',
    version='1.0.0',
    packages=['cli_anything.align'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-align=cli_anything.align:cli']},
)
