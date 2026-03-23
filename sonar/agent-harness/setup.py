from setuptools import setup
setup(
    name='cli-anything-sonar',
    version='1.0.0',
    packages=['cli_anything.sonar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sonar=cli_anything.sonar:cli']},
)
