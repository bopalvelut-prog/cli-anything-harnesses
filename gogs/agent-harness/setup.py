from setuptools import setup
setup(
    name='cli-anything-gogs',
    version='1.0.0',
    packages=['cli_anything.gogs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gogs=cli_anything.gogs:cli']},
)
