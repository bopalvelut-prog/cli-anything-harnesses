from setuptools import setup
setup(
    name='cli-anything-transformation',
    version='1.0.0',
    packages=['cli_anything.transformation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-transformation=cli_anything.transformation:cli']},
)
