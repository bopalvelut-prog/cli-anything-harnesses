from setuptools import setup
setup(
    name='cli-anything-issue',
    version='1.0.0',
    packages=['cli_anything.issue'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-issue=cli_anything.issue:cli']},
)
