from setuptools import setup
setup(
    name='cli-anything-bugsnag',
    version='1.0.0',
    packages=['cli_anything.bugsnag'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bugsnag=cli_anything.bugsnag:cli']},
)
