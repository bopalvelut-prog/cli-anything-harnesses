from setuptools import setup
setup(
    name='cli-anything-datahub',
    version='1.0.0',
    packages=['cli_anything.datahub'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-datahub=cli_anything.datahub:cli']},
)
