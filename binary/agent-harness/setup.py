from setuptools import setup
setup(
    name='cli-anything-binary',
    version='1.0.0',
    packages=['cli_anything.binary'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-binary=cli_anything.binary:cli']},
)
