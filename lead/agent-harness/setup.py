from setuptools import setup
setup(
    name='cli-anything-lead',
    version='1.0.0',
    packages=['cli_anything.lead'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lead=cli_anything.lead:cli']},
)
