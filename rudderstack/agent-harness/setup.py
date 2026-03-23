from setuptools import setup
setup(
    name='cli-anything-rudderstack',
    version='1.0.0',
    packages=['cli_anything.rudderstack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rudderstack=cli_anything.rudderstack:cli']},
)
