from setuptools import setup
setup(
    name='cli-anything-hour',
    version='1.0.0',
    packages=['cli_anything.hour'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hour=cli_anything.hour:cli']},
)
