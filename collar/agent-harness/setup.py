from setuptools import setup
setup(
    name='cli-anything-collar',
    version='1.0.0',
    packages=['cli_anything.collar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-collar=cli_anything.collar:cli']},
)
