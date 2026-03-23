from setuptools import setup
setup(
    name='cli-anything-camunda',
    version='1.0.0',
    packages=['cli_anything.camunda'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-camunda=cli_anything.camunda:cli']},
)
