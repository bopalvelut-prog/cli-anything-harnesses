from setuptools import setup
setup(
    name='cli-anything-trino',
    version='1.0.0',
    packages=['cli_anything.trino'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trino=cli_anything.trino:cli']},
)
