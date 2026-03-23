from setuptools import setup
setup(
    name='cli-anything-cprofile',
    version='1.0.0',
    packages=['cli_anything.cprofile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cprofile=cli_anything.cprofile:cli']},
)
