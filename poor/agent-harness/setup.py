from setuptools import setup
setup(
    name='cli-anything-poor',
    version='1.0.0',
    packages=['cli_anything.poor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-poor=cli_anything.poor:cli']},
)
