from setuptools import setup
setup(
    name='cli-anything-start',
    version='1.0.0',
    packages=['cli_anything.start'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-start=cli_anything.start:cli']},
)
