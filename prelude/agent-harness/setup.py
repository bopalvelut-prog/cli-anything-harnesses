from setuptools import setup
setup(
    name='cli-anything-prelude',
    version='1.0.0',
    packages=['cli_anything.prelude'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prelude=cli_anything.prelude:cli']},
)
