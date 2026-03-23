from setuptools import setup
setup(
    name='cli-anything-datastudio',
    version='1.0.0',
    packages=['cli_anything.datastudio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-datastudio=cli_anything.datastudio:cli']},
)
