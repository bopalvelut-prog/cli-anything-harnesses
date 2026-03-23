from setuptools import setup
setup(
    name='cli-anything-idp',
    version='1.0.0',
    packages=['cli_anything.idp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-idp=cli_anything.idp:cli']},
)
