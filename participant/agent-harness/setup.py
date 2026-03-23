from setuptools import setup
setup(
    name='cli-anything-participant',
    version='1.0.0',
    packages=['cli_anything.participant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-participant=cli_anything.participant:cli']},
)
