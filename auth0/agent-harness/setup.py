from setuptools import setup
setup(
    name='cli-anything-auth0',
    version='1.0.0',
    packages=['cli_anything.auth0'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-auth0=cli_anything.auth0:cli']},
)
