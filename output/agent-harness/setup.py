from setuptools import setup
setup(
    name='cli-anything-output',
    version='1.0.0',
    packages=['cli_anything.output'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-output=cli_anything.output:cli']},
)
