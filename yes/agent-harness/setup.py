from setuptools import setup
setup(
    name='cli-anything-yes',
    version='1.0.0',
    packages=['cli_anything.yes'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yes=cli_anything.yes:cli']},
)
