from setuptools import setup
setup(
    name='cli-anything-period',
    version='1.0.0',
    packages=['cli_anything.period'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-period=cli_anything.period:cli']},
)
