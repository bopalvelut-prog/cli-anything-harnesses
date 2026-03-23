from setuptools import setup
setup(
    name='cli-anything-pgcli',
    version='1.0.0',
    packages=['cli_anything.pgcli'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pgcli=cli_anything.pgcli:cli']},
)
