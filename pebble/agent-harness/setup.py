from setuptools import setup
setup(
    name='cli-anything-pebble',
    version='1.0.0',
    packages=['cli_anything.pebble'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pebble=cli_anything.pebble:cli']},
)
