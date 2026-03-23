from setuptools import setup
setup(
    name='cli-anything-blue',
    version='1.0.0',
    packages=['cli_anything.blue'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-blue=cli_anything.blue:cli']},
)
