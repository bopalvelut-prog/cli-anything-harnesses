from setuptools import setup
setup(
    name='cli-anything-spring',
    version='1.0.0',
    packages=['cli_anything.spring'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spring=cli_anything.spring:cli']},
)
