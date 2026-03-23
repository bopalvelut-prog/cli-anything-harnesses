from setuptools import setup
setup(
    name='cli-anything-source',
    version='1.0.0',
    packages=['cli_anything.source'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-source=cli_anything.source:cli']},
)
