from setuptools import setup
setup(
    name='cli-anything-atlassian',
    version='1.0.0',
    packages=['cli_anything.atlassian'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-atlassian=cli_anything.atlassian:cli']},
)
