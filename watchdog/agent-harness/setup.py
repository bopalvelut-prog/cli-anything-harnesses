from setuptools import setup
setup(
    name='cli-anything-watchdog',
    version='1.0.0',
    packages=['cli_anything.watchdog'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-watchdog=cli_anything.watchdog:cli']},
)
