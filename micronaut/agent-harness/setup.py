from setuptools import setup
setup(
    name='cli-anything-micronaut',
    version='1.0.0',
    packages=['cli_anything.micronaut'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-micronaut=cli_anything.micronaut:cli']},
)
