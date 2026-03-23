from setuptools import setup
setup(
    name='cli-anything-calendar',
    version='1.0.0',
    packages=['cli_anything.calendar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-calendar=cli_anything.calendar:cli']},
)
