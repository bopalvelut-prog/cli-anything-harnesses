from setuptools import setup
setup(
    name='cli-anything-vitess',
    version='1.0.0',
    packages=['cli_anything.vitess'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vitess=cli_anything.vitess:cli']},
)
