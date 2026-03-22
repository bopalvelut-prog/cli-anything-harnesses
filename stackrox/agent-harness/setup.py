from setuptools import setup
setup(
    name='cli-anything-stackrox',
    version='1.0.0',
    packages=['cli_anything.stackrox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stackrox=cli_anything.stackrox:cli']},
)
