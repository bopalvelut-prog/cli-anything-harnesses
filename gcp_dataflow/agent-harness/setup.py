from setuptools import setup
setup(
    name='cli-anything-gcp_dataflow',
    version='1.0.0',
    packages=['cli_anything.gcp_dataflow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_dataflow=cli_anything.gcp_dataflow:cli']},
)
