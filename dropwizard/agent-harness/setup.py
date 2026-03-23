from setuptools import setup
setup(
    name='cli-anything-dropwizard',
    version='1.0.0',
    packages=['cli_anything.dropwizard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dropwizard=cli_anything.dropwizard:cli']},
)
