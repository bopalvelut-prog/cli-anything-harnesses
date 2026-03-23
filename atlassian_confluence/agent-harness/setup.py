from setuptools import setup
setup(
    name='cli-anything-atlassian_confluence',
    version='1.0.0',
    packages=['cli_anything.atlassian_confluence'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-atlassian_confluence=cli_anything.atlassian_confluence:cli']},
)
