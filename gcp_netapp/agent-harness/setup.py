from setuptools import setup
setup(
    name='cli-anything-gcp_netapp',
    version='1.0.0',
    packages=['cli_anything.gcp_netapp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_netapp=cli_anything.gcp_netapp:cli']},
)
