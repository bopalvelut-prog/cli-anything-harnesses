from setuptools import setup
setup(
    name='cli-anything-red',
    version='1.0.0',
    packages=['cli_anything.red'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-red=cli_anything.red:cli']},
)
