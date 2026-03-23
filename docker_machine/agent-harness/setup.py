from setuptools import setup
setup(
    name='cli-anything-docker_machine',
    version='1.0.0',
    packages=['cli_anything.docker_machine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-docker_machine=cli_anything.docker_machine:cli']},
)
