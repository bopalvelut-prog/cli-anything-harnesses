from setuptools import setup
setup(
    name='cli-anything-trend',
    version='1.0.0',
    packages=['cli_anything.trend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trend=cli_anything.trend:cli']},
)
