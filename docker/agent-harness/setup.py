from setuptools import setup
setup(
    name='cli-anything-docker',
    version='1.0.0',
    packages=['cli_anything.docker'],
    install_requires=['click', 'docker'],
    entry_points={'console_scripts': ['cli-anything-docker=cli_anything.docker:cli']},
)
