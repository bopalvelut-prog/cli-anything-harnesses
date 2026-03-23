from setuptools import setup
setup(
    name='cli-anything-challenge',
    version='1.0.0',
    packages=['cli_anything.challenge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-challenge=cli_anything.challenge:cli']},
)
