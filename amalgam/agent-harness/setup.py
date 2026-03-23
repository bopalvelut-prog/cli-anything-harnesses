from setuptools import setup
setup(
    name='cli-anything-amalgam',
    version='1.0.0',
    packages=['cli_anything.amalgam'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amalgam=cli_anything.amalgam:cli']},
)
