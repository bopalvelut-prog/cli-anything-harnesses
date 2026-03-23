from setuptools import setup
setup(
    name='cli-anything-carp',
    version='1.0.0',
    packages=['cli_anything.carp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-carp=cli_anything.carp:cli']},
)
