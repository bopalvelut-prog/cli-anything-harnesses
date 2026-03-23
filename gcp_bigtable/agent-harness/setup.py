from setuptools import setup
setup(
    name='cli-anything-gcp_bigtable',
    version='1.0.0',
    packages=['cli_anything.gcp_bigtable'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_bigtable=cli_anything.gcp_bigtable:cli']},
)
