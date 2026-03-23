from setuptools import setup
setup(
    name='cli-anything-terms',
    version='1.0.0',
    packages=['cli_anything.terms'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-terms=cli_anything.terms:cli']},
)
