from setuptools import setup
setup(
    name='cli-anything-can',
    version='1.0.0',
    packages=['cli_anything.can'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-can=cli_anything.can:cli']},
)
