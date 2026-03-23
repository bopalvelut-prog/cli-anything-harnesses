from setuptools import setup
setup(
    name='cli-anything-apollo_client',
    version='1.0.0',
    packages=['cli_anything.apollo_client'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apollo_client=cli_anything.apollo_client:cli']},
)
