from setuptools import setup
setup(
    name='cli-anything-gcp_compute',
    version='1.0.0',
    packages=['cli_anything.gcp_compute'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_compute=cli_anything.gcp_compute:cli']},
)
