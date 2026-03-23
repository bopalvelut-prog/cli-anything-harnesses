from setuptools import setup
setup(
    name='cli-anything-gcp_endpoints',
    version='1.0.0',
    packages=['cli_anything.gcp_endpoints'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_endpoints=cli_anything.gcp_endpoints:cli']},
)
