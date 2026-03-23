from setuptools import setup
setup(
    name='cli-anything-weird',
    version='1.0.0',
    packages=['cli_anything.weird'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-weird=cli_anything.weird:cli']},
)
