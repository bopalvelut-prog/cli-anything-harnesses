from setuptools import setup
setup(
    name='cli-anything-bolt',
    version='1.0.0',
    packages=['cli_anything.bolt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bolt=cli_anything.bolt:cli']},
)
