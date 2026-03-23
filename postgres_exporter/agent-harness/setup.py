from setuptools import setup
setup(
    name='cli-anything-postgres_exporter',
    version='1.0.0',
    packages=['cli_anything.postgres_exporter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-postgres_exporter=cli_anything.postgres_exporter:cli']},
)
