from setuptools import setup
setup(
    name='cli-anything-floor',
    version='1.0.0',
    packages=['cli_anything.floor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-floor=cli_anything.floor:cli']},
)
