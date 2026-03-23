from setuptools import setup
setup(
    name='cli-anything-relation',
    version='1.0.0',
    packages=['cli_anything.relation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-relation=cli_anything.relation:cli']},
)
