from setuptools import setup
setup(
    name='cli-anything-examine',
    version='1.0.0',
    packages=['cli_anything.examine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-examine=cli_anything.examine:cli']},
)
