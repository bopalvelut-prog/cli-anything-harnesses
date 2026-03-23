from setuptools import setup
setup(
    name='cli-anything-pushover',
    version='1.0.0',
    packages=['cli_anything.pushover'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pushover=cli_anything.pushover:cli']},
)
