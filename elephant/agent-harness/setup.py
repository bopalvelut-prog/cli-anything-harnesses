from setuptools import setup
setup(
    name='cli-anything-elephant',
    version='1.0.0',
    packages=['cli_anything.elephant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-elephant=cli_anything.elephant:cli']},
)
