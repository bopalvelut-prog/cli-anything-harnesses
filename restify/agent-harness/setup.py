from setuptools import setup
setup(
    name='cli-anything-restify',
    version='1.0.0',
    packages=['cli_anything.restify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-restify=cli_anything.restify:cli']},
)
