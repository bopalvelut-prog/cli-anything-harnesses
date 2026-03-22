from setuptools import setup
setup(
    name='cli-anything-commvault',
    version='1.0.0',
    packages=['cli_anything.commvault'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-commvault=cli_anything.commvault:cli']},
)
