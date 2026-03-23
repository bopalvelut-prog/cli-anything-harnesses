from setuptools import setup
setup(
    name='cli-anything-diagrams',
    version='1.0.0',
    packages=['cli_anything.diagrams'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-diagrams=cli_anything.diagrams:cli']},
)
