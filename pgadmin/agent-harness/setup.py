from setuptools import setup
setup(
    name='cli-anything-pgadmin',
    version='1.0.0',
    packages=['cli_anything.pgadmin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pgadmin=cli_anything.pgadmin:cli']},
)
