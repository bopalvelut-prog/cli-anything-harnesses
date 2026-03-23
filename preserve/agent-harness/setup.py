from setuptools import setup
setup(
    name='cli-anything-preserve',
    version='1.0.0',
    packages=['cli_anything.preserve'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-preserve=cli_anything.preserve:cli']},
)
