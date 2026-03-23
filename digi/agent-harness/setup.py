from setuptools import setup
setup(
    name='cli-anything-digi',
    version='1.0.0',
    packages=['cli_anything.digi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-digi=cli_anything.digi:cli']},
)
