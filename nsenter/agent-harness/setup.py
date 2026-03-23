from setuptools import setup
setup(
    name='cli-anything-nsenter',
    version='1.0.0',
    packages=['cli_anything.nsenter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nsenter=cli_anything.nsenter:cli']},
)
