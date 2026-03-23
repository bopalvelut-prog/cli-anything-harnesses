from setuptools import setup
setup(
    name='cli-anything-tissue',
    version='1.0.0',
    packages=['cli_anything.tissue'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tissue=cli_anything.tissue:cli']},
)
