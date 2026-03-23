from setuptools import setup
setup(
    name='cli-anything-paddle',
    version='1.0.0',
    packages=['cli_anything.paddle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-paddle=cli_anything.paddle:cli']},
)
