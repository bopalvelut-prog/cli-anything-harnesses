from setuptools import setup
setup(
    name='cli-anything-ontology',
    version='1.0.0',
    packages=['cli_anything.ontology'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ontology=cli_anything.ontology:cli']},
)
