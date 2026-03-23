from setuptools import setup
setup(
    name='cli-anything-respond',
    version='1.0.0',
    packages=['cli_anything.respond'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-respond=cli_anything.respond:cli']},
)
