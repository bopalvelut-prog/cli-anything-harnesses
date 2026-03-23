from setuptools import setup
setup(
    name='cli-anything-dalle',
    version='1.0.0',
    packages=['cli_anything.dalle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dalle=cli_anything.dalle:cli']},
)
