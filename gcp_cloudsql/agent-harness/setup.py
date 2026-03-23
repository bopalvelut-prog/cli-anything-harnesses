from setuptools import setup
setup(
    name='cli-anything-gcp_cloudsql',
    version='1.0.0',
    packages=['cli_anything.gcp_cloudsql'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_cloudsql=cli_anything.gcp_cloudsql:cli']},
)
