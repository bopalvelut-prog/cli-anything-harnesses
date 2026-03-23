from setuptools import setup
setup(
    name='cli-anything-elastic',
    version='1.0.0',
    packages=['cli_anything.elastic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-elastic=cli_anything.elastic:cli']},
)
