from setuptools import setup
setup(
    name='cli-anything-nipap',
    version='1.0.0',
    packages=['cli_anything.nipap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nipap=cli_anything.nipap:cli']},
)
