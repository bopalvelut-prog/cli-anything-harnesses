from setuptools import setup
setup(
    name='cli-anything-gradle',
    version='1.0.0',
    packages=['cli_anything.gradle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gradle=cli_anything.gradle:cli']},
)
