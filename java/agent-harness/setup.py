from setuptools import setup
setup(
    name='cli-anything-java',
    version='1.0.0',
    packages=['cli_anything.java'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-java=cli_anything.java:cli']},
)
