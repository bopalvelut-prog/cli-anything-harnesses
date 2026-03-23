from setuptools import setup
setup(
    name='cli-anything-gcp_dataproc',
    version='1.0.0',
    packages=['cli_anything.gcp_dataproc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_dataproc=cli_anything.gcp_dataproc:cli']},
)
