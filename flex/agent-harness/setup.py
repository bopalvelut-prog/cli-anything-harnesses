from setuptools import setup
setup(
    name='cli-anything-flex',
    version='1.0.0',
    packages=['cli_anything.flex'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flex=cli_anything.flex:cli']},
)
