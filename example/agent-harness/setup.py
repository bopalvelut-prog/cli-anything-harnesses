from setuptools import setup
setup(
    name='cli-anything-example',
    version='1.0.0',
    packages=['cli_anything.example'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-example=cli_anything.example:cli']},
)
