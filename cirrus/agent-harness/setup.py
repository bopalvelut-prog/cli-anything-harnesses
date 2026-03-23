from setuptools import setup
setup(
    name='cli-anything-cirrus',
    version='1.0.0',
    packages=['cli_anything.cirrus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cirrus=cli_anything.cirrus:cli']},
)
