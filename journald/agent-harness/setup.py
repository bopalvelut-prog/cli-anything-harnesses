from setuptools import setup
setup(
    name='cli-anything-journald',
    version='1.0.0',
    packages=['cli_anything.journald'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-journald=cli_anything.journald:cli']},
)
