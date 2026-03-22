from setuptools import setup
setup(
    name='cli-anything-chronograf',
    version='1.0.0',
    packages=['cli_anything.chronograf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chronograf=cli_anything.chronograf:cli']},
)
