from setuptools import setup
setup(
    name='cli-anything-boxfuse',
    version='1.0.0',
    packages=['cli_anything.boxfuse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-boxfuse=cli_anything.boxfuse:cli']},
)
