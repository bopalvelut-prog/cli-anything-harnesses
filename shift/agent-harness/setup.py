from setuptools import setup
setup(
    name='cli-anything-shift',
    version='1.0.0',
    packages=['cli_anything.shift'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shift=cli_anything.shift:cli']},
)
