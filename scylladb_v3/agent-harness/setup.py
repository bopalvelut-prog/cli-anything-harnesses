from setuptools import setup
setup(
    name='cli-anything-scylladb_v3',
    version='1.0.0',
    packages=['cli_anything.scylladb_v3'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scylladb_v3=cli_anything.scylladb_v3:cli']},
)
