from setuptools import setup
setup(
    name='cli-anything-docker_swarm',
    version='1.0.0',
    packages=['cli_anything.docker_swarm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-docker_swarm=cli_anything.docker_swarm:cli']},
)
