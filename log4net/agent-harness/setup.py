from setuptools import setup
setup(
    name='cli-anything-log4net',
    version='1.0.0',
    packages=['cli_anything.log4net'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-log4net=cli_anything.log4net:cli']},
)
