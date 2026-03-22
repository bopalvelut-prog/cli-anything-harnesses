from setuptools import setup
setup(
    name='cli-anything-docusaurus',
    version='1.0.0',
    packages=['cli_anything.docusaurus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-docusaurus=cli_anything.docusaurus:cli']},
)
