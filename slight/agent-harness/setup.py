from setuptools import setup
setup(
    name='cli-anything-slight',
    version='1.0.0',
    packages=['cli_anything.slight'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slight=cli_anything.slight:cli']},
)
