from setuptools import setup
setup(
    name='cli-anything-golangci',
    version='1.0.0',
    packages=['cli_anything.golangci'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-golangci=cli_anything.golangci:cli']},
)
