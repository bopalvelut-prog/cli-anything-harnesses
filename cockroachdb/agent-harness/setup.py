from setuptools import setup
setup(
    name='cli-anything-cockroachdb',
    version='1.0.0',
    packages=['cli_anything.cockroachdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cockroachdb=cli_anything.cockroachdb:cli']},
)
