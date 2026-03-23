from setuptools import setup
setup(
    name='cli-anything-palantir',
    version='1.0.0',
    packages=['cli_anything.palantir'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-palantir=cli_anything.palantir:cli']},
)
