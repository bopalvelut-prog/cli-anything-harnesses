from setuptools import setup
setup(
    name='cli-anything-jenkinsfile',
    version='1.0.0',
    packages=['cli_anything.jenkinsfile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jenkinsfile=cli_anything.jenkinsfile:cli']},
)
