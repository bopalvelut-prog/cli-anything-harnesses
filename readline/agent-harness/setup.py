from setuptools import setup
setup(
    name='cli-anything-readline',
    version='1.0.0',
    packages=['cli_anything.readline'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-readline=cli_anything.readline:cli']},
)
