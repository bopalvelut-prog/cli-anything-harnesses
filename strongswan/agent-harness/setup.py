from setuptools import setup
setup(
    name='cli-anything-strongswan',
    version='1.0.0',
    packages=['cli_anything.strongswan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-strongswan=cli_anything.strongswan:cli']},
)
