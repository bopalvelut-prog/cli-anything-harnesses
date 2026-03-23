from setuptools import setup
setup(
    name='cli-anything-objectbox',
    version='1.0.0',
    packages=['cli_anything.objectbox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-objectbox=cli_anything.objectbox:cli']},
)
