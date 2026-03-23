from setuptools import setup
setup(
    name='cli-anything-football',
    version='1.0.0',
    packages=['cli_anything.football'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-football=cli_anything.football:cli']},
)
