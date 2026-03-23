from setuptools import setup
setup(
    name='cli-anything-phabricator',
    version='1.0.0',
    packages=['cli_anything.phabricator'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-phabricator=cli_anything.phabricator:cli']},
)
