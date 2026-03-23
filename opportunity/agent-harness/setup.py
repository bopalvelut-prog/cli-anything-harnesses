from setuptools import setup
setup(
    name='cli-anything-opportunity',
    version='1.0.0',
    packages=['cli_anything.opportunity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-opportunity=cli_anything.opportunity:cli']},
)
