from setuptools import setup
setup(
    name='cli-anything-gcp_run',
    version='1.0.0',
    packages=['cli_anything.gcp_run'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_run=cli_anything.gcp_run:cli']},
)
