from setuptools import setup
setup(
    name='cli-anything-acme',
    version='1.0.0',
    packages=['cli_anything.acme'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-acme=cli_anything.acme:cli']},
)
