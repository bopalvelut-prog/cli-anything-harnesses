from setuptools import setup
setup(
    name='cli-anything-marshmallow',
    version='1.0.0',
    packages=['cli_anything.marshmallow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-marshmallow=cli_anything.marshmallow:cli']},
)
