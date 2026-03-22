from setuptools import setup
setup(
    name='cli-anything-balancer',
    version='1.0.0',
    packages=['cli_anything.balancer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-balancer=cli_anything.balancer:cli']},
)
