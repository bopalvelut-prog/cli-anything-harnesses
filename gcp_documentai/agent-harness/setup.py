from setuptools import setup
setup(
    name='cli-anything-gcp_documentai',
    version='1.0.0',
    packages=['cli_anything.gcp_documentai'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_documentai=cli_anything.gcp_documentai:cli']},
)
