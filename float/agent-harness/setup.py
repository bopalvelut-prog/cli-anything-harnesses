from setuptools import setup
setup(
    name='cli-anything-float',
    version='1.0.0',
    packages=['cli_anything.float'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-float=cli_anything.float:cli']},
)
