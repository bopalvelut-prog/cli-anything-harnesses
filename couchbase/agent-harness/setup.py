from setuptools import setup
setup(
    name='cli-anything-couchbase',
    version='1.0.0',
    packages=['cli_anything.couchbase'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-couchbase=cli_anything.couchbase:cli']},
)
