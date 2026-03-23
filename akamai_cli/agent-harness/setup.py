from setuptools import setup
setup(
    name='cli-anything-akamai_cli',
    version='1.0.0',
    packages=['cli_anything.akamai_cli'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-akamai_cli=cli_anything.akamai_cli:cli']},
)
