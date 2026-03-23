from setuptools import setup
setup(
    name='cli-anything-benthos',
    version='1.0.0',
    packages=['cli_anything.benthos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-benthos=cli_anything.benthos:cli']},
)
