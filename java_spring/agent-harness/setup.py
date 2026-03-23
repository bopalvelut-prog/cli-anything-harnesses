from setuptools import setup
setup(
    name='cli-anything-java_spring',
    version='1.0.0',
    packages=['cli_anything.java_spring'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-java_spring=cli_anything.java_spring:cli']},
)
