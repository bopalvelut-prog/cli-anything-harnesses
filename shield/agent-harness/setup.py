from setuptools import setup
setup(
    name='cli-anything-shield',
    version='1.0.0',
    packages=['cli_anything.shield'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shield=cli_anything.shield:cli']},
)
