from setuptools import setup
setup(
    name='cli-anything-gcp_bigquery',
    version='1.0.0',
    packages=['cli_anything.gcp_bigquery'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_bigquery=cli_anything.gcp_bigquery:cli']},
)
