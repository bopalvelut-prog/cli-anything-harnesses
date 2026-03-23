from setuptools import setup
setup(
    name='cli-anything-leap',
    version='1.0.0',
    packages=['cli_anything.leap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-leap=cli_anything.leap:cli']},
)
