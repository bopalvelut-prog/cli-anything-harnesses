from setuptools import setup
setup(
    name='cli-anything-negative',
    version='1.0.0',
    packages=['cli_anything.negative'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-negative=cli_anything.negative:cli']},
)
