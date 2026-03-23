from setuptools import setup
setup(
    name='cli-anything-apollo_federation',
    version='1.0.0',
    packages=['cli_anything.apollo_federation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apollo_federation=cli_anything.apollo_federation:cli']},
)
