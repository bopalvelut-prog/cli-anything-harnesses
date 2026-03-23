from setuptools import setup
setup(
    name='cli-anything-virtual',
    version='1.0.0',
    packages=['cli_anything.virtual'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-virtual=cli_anything.virtual:cli']},
)
