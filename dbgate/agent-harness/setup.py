from setuptools import setup
setup(
    name='cli-anything-dbgate',
    version='1.0.0',
    packages=['cli_anything.dbgate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dbgate=cli_anything.dbgate:cli']},
)
