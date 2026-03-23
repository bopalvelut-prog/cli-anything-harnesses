from setuptools import setup
setup(
    name='cli-anything-spacy',
    version='1.0.0',
    packages=['cli_anything.spacy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spacy=cli_anything.spacy:cli']},
)
