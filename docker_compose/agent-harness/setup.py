from setuptools import setup
setup(
    name='cli-anything-docker_compose',
    version='1.0.0',
    packages=['cli_anything.docker_compose'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-docker_compose=cli_anything.docker_compose:cli']},
)
