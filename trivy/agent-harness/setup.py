from setuptools import setup
setup(
    name='cli-anything-trivy',
    version='1.0.0',
    packages=['cli_anything.trivy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trivy=cli_anything.trivy:cli']},
)
