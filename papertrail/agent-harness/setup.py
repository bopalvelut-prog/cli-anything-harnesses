from setuptools import setup
setup(
    name='cli-anything-papertrail',
    version='1.0.0',
    packages=['cli_anything.papertrail'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-papertrail=cli_anything.papertrail:cli']},
)
