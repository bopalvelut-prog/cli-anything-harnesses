from setuptools import setup
setup(
    name='cli-anything-codelabs',
    version='1.0.0',
    packages=['cli_anything.codelabs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-codelabs=cli_anything.codelabs:cli']},
)
