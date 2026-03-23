from setuptools import setup
setup(
    name='cli-anything-terrorism',
    version='1.0.0',
    packages=['cli_anything.terrorism'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-terrorism=cli_anything.terrorism:cli']},
)
