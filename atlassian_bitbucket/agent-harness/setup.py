from setuptools import setup
setup(
    name='cli-anything-atlassian_bitbucket',
    version='1.0.0',
    packages=['cli_anything.atlassian_bitbucket'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-atlassian_bitbucket=cli_anything.atlassian_bitbucket:cli']},
)
