from setuptools import setup
setup(
    name='cli-anything-sonarqube',
    version='1.0.0',
    packages=['cli_anything.sonarqube'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sonarqube=cli_anything.sonarqube:cli']},
)
