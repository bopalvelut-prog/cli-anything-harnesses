from setuptools import setup
setup(
    name='cli-anything-osquery',
    version='1.0.0',
    packages=['cli_anything.osquery'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-osquery=cli_anything.osquery:cli']},
)
