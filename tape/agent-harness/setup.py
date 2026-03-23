from setuptools import setup
setup(
    name='cli-anything-tape',
    version='1.0.0',
    packages=['cli_anything.tape'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tape=cli_anything.tape:cli']},
)
