from setuptools import setup
setup(
    name='cli-anything-loadbalancer',
    version='1.0.0',
    packages=['cli_anything.loadbalancer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-loadbalancer=cli_anything.loadbalancer:cli']},
)
