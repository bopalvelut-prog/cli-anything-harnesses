from setuptools import setup
setup(
    name='cli-anything-cayley',
    version='1.0.0',
    packages=['cli_anything.cayley'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cayley=cli_anything.cayley:cli']},
)
