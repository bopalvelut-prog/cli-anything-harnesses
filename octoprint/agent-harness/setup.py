from setuptools import setup
setup(
    name='cli-anything-octoprint',
    version='1.0.0',
    packages=['cli_anything.octoprint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-octoprint=cli_anything.octoprint:cli']},
)
