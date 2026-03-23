from setuptools import setup
setup(
    name='cli-anything-artifactory',
    version='1.0.0',
    packages=['cli_anything.artifactory'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-artifactory=cli_anything.artifactory:cli']},
)
