from setuptools import setup
setup(
    name='cli-anything-salesforce',
    version='1.0.0',
    packages=['cli_anything.salesforce'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-salesforce=cli_anything.salesforce:cli']},
)
