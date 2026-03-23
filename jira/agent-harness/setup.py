from setuptools import setup
setup(
    name='cli-anything-jira',
    version='1.0.0',
    packages=['cli_anything.jira'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jira=cli_anything.jira:cli']},
)
