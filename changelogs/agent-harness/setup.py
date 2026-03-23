from setuptools import setup
setup(
    name='cli-anything-changelogs',
    version='1.0.0',
    packages=['cli_anything.changelogs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-changelogs=cli_anything.changelogs:cli']},
)
