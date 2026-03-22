from setuptools import setup
setup(
    name='cli-anything-payload',
    version='1.0.0',
    packages=['cli_anything.payload'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-payload=cli_anything.payload:cli']},
)
