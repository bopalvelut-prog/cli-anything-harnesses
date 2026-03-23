from setuptools import setup
setup(
    name='cli-anything-pink',
    version='1.0.0',
    packages=['cli_anything.pink'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pink=cli_anything.pink:cli']},
)
