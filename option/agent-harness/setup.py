from setuptools import setup
setup(
    name='cli-anything-option',
    version='1.0.0',
    packages=['cli_anything.option'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-option=cli_anything.option:cli']},
)
