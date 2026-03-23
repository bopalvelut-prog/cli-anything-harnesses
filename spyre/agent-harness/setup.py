from setuptools import setup
setup(
    name='cli-anything-spyre',
    version='1.0.0',
    packages=['cli_anything.spyre'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spyre=cli_anything.spyre:cli']},
)
