from setuptools import setup
setup(
    name='cli-anything-moderator',
    version='1.0.0',
    packages=['cli_anything.moderator'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-moderator=cli_anything.moderator:cli']},
)
