from setuptools import setup
setup(
    name='cli-anything-block',
    version='1.0.0',
    packages=['cli_anything.block'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-block=cli_anything.block:cli']},
)
