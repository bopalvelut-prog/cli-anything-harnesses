from setuptools import setup
setup(
    name='cli-anything-yet',
    version='1.0.0',
    packages=['cli_anything.yet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yet=cli_anything.yet:cli']},
)
