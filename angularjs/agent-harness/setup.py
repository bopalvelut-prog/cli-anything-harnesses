from setuptools import setup
setup(
    name='cli-anything-angularjs',
    version='1.0.0',
    packages=['cli_anything.angularjs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-angularjs=cli_anything.angularjs:cli']},
)
