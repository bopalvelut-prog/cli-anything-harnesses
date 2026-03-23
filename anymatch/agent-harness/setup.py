from setuptools import setup
setup(
    name='cli-anything-anymatch',
    version='1.0.0',
    packages=['cli_anything.anymatch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-anymatch=cli_anything.anymatch:cli']},
)
