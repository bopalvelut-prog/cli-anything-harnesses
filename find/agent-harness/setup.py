from setuptools import setup
setup(
    name='cli-anything-find',
    version='1.0.0',
    packages=['cli_anything.find'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-find=cli_anything.find:cli']},
)
