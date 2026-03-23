from setuptools import setup
setup(
    name='cli-anything-gcp_spanner',
    version='1.0.0',
    packages=['cli_anything.gcp_spanner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_spanner=cli_anything.gcp_spanner:cli']},
)
