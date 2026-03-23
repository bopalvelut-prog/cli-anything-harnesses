from setuptools import setup
setup(
    name='cli-anything-querybuilder',
    version='1.0.0',
    packages=['cli_anything.querybuilder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-querybuilder=cli_anything.querybuilder:cli']},
)
