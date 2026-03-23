from setuptools import setup
setup(
    name='cli-anything-waffle',
    version='1.0.0',
    packages=['cli_anything.waffle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-waffle=cli_anything.waffle:cli']},
)
