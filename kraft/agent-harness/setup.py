from setuptools import setup
setup(
    name='cli-anything-kraft',
    version='1.0.0',
    packages=['cli_anything.kraft'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kraft=cli_anything.kraft:cli']},
)
