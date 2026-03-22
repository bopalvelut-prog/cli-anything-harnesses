from setuptools import setup
setup(
    name='cli-anything-timeshift',
    version='1.0.0',
    packages=['cli_anything.timeshift'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-timeshift=cli_anything.timeshift:cli']},
)
