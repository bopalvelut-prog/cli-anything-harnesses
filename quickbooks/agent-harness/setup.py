from setuptools import setup
setup(
    name='cli-anything-quickbooks',
    version='1.0.0',
    packages=['cli_anything.quickbooks'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quickbooks=cli_anything.quickbooks:cli']},
)
