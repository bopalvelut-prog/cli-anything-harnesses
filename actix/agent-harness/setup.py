from setuptools import setup
setup(
    name='cli-anything-actix',
    version='1.0.0',
    packages=['cli_anything.actix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-actix=cli_anything.actix:cli']},
)
