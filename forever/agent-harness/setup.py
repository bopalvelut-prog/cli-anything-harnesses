from setuptools import setup
setup(
    name='cli-anything-forever',
    version='1.0.0',
    packages=['cli_anything.forever'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-forever=cli_anything.forever:cli']},
)
