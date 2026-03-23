from setuptools import setup
setup(
    name='cli-anything-slackware',
    version='1.0.0',
    packages=['cli_anything.slackware'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slackware=cli_anything.slackware:cli']},
)
