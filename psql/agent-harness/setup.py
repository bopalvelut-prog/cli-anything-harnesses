from setuptools import setup
setup(
    name='cli-anything-psql',
    version='1.0.0',
    packages=['cli_anything.psql'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-psql=cli_anything.psql:cli']},
)
