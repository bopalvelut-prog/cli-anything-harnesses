from setuptools import setup
setup(
    name='cli-anything-rural',
    version='1.0.0',
    packages=['cli_anything.rural'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rural=cli_anything.rural:cli']},
)
