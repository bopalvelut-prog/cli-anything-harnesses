from setuptools import setup
setup(
    name='cli-anything-hurry',
    version='1.0.0',
    packages=['cli_anything.hurry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hurry=cli_anything.hurry:cli']},
)
