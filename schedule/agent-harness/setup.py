from setuptools import setup
setup(
    name='cli-anything-schedule',
    version='1.0.0',
    packages=['cli_anything.schedule'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-schedule=cli_anything.schedule:cli']},
)
