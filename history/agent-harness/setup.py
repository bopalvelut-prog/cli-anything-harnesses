from setuptools import setup
setup(
    name='cli-anything-history',
    version='1.0.0',
    packages=['cli_anything.history'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-history=cli_anything.history:cli']},
)
