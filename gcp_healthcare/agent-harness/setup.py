from setuptools import setup
setup(
    name='cli-anything-gcp_healthcare',
    version='1.0.0',
    packages=['cli_anything.gcp_healthcare'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_healthcare=cli_anything.gcp_healthcare:cli']},
)
