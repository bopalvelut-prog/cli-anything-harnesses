from setuptools import setup
setup(
    name='cli-anything-bare',
    version='1.0.0',
    packages=['cli_anything.bare'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bare=cli_anything.bare:cli']},
)
