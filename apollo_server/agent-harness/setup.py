from setuptools import setup
setup(
    name='cli-anything-apollo_server',
    version='1.0.0',
    packages=['cli_anything.apollo_server'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apollo_server=cli_anything.apollo_server:cli']},
)
