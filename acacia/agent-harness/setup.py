from setuptools import setup
setup(
    name='cli-anything-acacia',
    version='1.0.0',
    packages=['cli_anything.acacia'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-acacia=cli_anything.acacia:cli']},
)
