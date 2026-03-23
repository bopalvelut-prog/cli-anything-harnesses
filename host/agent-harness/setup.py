from setuptools import setup
setup(
    name='cli-anything-host',
    version='1.0.0',
    packages=['cli_anything.host'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-host=cli_anything.host:cli']},
)
