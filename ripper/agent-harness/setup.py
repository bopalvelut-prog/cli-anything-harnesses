from setuptools import setup
setup(
    name='cli-anything-ripper',
    version='1.0.0',
    packages=['cli_anything.ripper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ripper=cli_anything.ripper:cli']},
)
