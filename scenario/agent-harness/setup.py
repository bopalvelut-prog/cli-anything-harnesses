from setuptools import setup
setup(
    name='cli-anything-scenario',
    version='1.0.0',
    packages=['cli_anything.scenario'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scenario=cli_anything.scenario:cli']},
)
