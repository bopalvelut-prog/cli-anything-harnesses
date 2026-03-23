from setuptools import setup
setup(
    name='cli-anything-pgbouncer',
    version='1.0.0',
    packages=['cli_anything.pgbouncer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pgbouncer=cli_anything.pgbouncer:cli']},
)
