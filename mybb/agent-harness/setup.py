from setuptools import setup
setup(
    name='cli-anything-mybb',
    version='1.0.0',
    packages=['cli_anything.mybb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mybb=cli_anything.mybb:cli']},
)
