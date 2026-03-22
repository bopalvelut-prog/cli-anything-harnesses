from setuptools import setup
setup(
    name='cli-anything-docker_bench',
    version='1.0.0',
    packages=['cli_anything.docker_bench'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-docker_bench=cli_anything.docker_bench:cli']},
)
