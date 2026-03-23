from setuptools import setup
setup(
    name='cli-anything-heaven',
    version='1.0.0',
    packages=['cli_anything.heaven'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-heaven=cli_anything.heaven:cli']},
)
