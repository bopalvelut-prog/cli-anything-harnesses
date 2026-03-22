from setuptools import setup
setup(
    name='cli-anything-dokku',
    version='1.0.0',
    packages=['cli_anything.dokku'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dokku=cli_anything.dokku:cli']},
)
