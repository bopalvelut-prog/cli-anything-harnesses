from setuptools import setup
setup(
    name='cli-anything-folk',
    version='1.0.0',
    packages=['cli_anything.folk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-folk=cli_anything.folk:cli']},
)
