from setuptools import setup
setup(
    name='cli-anything-atlassian_jira',
    version='1.0.0',
    packages=['cli_anything.atlassian_jira'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-atlassian_jira=cli_anything.atlassian_jira:cli']},
)
