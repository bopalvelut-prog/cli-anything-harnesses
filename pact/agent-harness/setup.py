from setuptools import setup
setup(
    name='cli-anything-pact',
    version='1.0.0',
    packages=['cli_anything.pact'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pact=cli_anything.pact:cli']},
)
