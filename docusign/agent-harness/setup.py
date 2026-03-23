from setuptools import setup
setup(
    name='cli-anything-docusign',
    version='1.0.0',
    packages=['cli_anything.docusign'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-docusign=cli_anything.docusign:cli']},
)
