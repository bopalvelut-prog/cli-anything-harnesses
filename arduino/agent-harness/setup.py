from setuptools import setup
setup(
    name='cli-anything-arduino',
    version='1.0.0',
    packages=['cli_anything.arduino'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-arduino=cli_anything.arduino:cli']},
)
