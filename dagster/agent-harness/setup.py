from setuptools import setup
setup(
    name='cli-anything-dagster',
    version='1.0.0',
    packages=['cli_anything.dagster'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dagster=cli_anything.dagster:cli']},
)
