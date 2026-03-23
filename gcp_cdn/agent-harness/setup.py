from setuptools import setup
setup(
    name='cli-anything-gcp_cdn',
    version='1.0.0',
    packages=['cli_anything.gcp_cdn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_cdn=cli_anything.gcp_cdn:cli']},
)
