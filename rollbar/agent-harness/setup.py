from setuptools import setup
setup(
    name='cli-anything-rollbar',
    version='1.0.0',
    packages=['cli_anything.rollbar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rollbar=cli_anything.rollbar:cli']},
)
