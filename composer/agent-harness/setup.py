from setuptools import setup
setup(
    name='cli-anything-composer',
    version='1.0.0',
    packages=['cli_anything.composer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-composer=cli_anything.composer:cli']},
)
