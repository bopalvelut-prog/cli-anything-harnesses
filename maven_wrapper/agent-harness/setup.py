from setuptools import setup
setup(
    name='cli-anything-maven_wrapper',
    version='1.0.0',
    packages=['cli_anything.maven_wrapper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-maven_wrapper=cli_anything.maven_wrapper:cli']},
)
