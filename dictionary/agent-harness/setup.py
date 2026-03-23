from setuptools import setup
setup(
    name='cli-anything-dictionary',
    version='1.0.0',
    packages=['cli_anything.dictionary'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dictionary=cli_anything.dictionary:cli']},
)
