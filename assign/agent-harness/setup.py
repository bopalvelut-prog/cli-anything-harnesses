from setuptools import setup
setup(
    name='cli-anything-assign',
    version='1.0.0',
    packages=['cli_anything.assign'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-assign=cli_anything.assign:cli']},
)
