from setuptools import setup
setup(
    name='cli-anything-later',
    version='1.0.0',
    packages=['cli_anything.later'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-later=cli_anything.later:cli']},
)
