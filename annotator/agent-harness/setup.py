from setuptools import setup
setup(
    name='cli-anything-annotator',
    version='1.0.0',
    packages=['cli_anything.annotator'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-annotator=cli_anything.annotator:cli']},
)
