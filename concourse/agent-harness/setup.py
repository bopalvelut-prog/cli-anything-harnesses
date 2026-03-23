from setuptools import setup
setup(
    name='cli-anything-concourse',
    version='1.0.0',
    packages=['cli_anything.concourse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-concourse=cli_anything.concourse:cli']},
)
