from setuptools import setup
setup(
    name='cli-anything-csscomb',
    version='1.0.0',
    packages=['cli_anything.csscomb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-csscomb=cli_anything.csscomb:cli']},
)
