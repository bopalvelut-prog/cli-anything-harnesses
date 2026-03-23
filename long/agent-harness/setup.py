from setuptools import setup
setup(
    name='cli-anything-long',
    version='1.0.0',
    packages=['cli_anything.long'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-long=cli_anything.long:cli']},
)
