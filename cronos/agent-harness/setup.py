from setuptools import setup
setup(
    name='cli-anything-cronos',
    version='1.0.0',
    packages=['cli_anything.cronos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cronos=cli_anything.cronos:cli']},
)
