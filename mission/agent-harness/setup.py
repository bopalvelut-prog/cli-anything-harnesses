from setuptools import setup
setup(
    name='cli-anything-mission',
    version='1.0.0',
    packages=['cli_anything.mission'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mission=cli_anything.mission:cli']},
)
