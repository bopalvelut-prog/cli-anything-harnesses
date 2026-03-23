from setuptools import setup
setup(
    name='cli-anything-cluster',
    version='1.0.0',
    packages=['cli_anything.cluster'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cluster=cli_anything.cluster:cli']},
)
