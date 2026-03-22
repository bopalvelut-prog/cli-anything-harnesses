from setuptools import setup
setup(
    name='cli-anything-freshdesk',
    version='1.0.0',
    packages=['cli_anything.freshdesk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-freshdesk=cli_anything.freshdesk:cli']},
)
