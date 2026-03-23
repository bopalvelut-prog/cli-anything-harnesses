from setuptools import setup
setup(
    name='cli-anything-southern',
    version='1.0.0',
    packages=['cli_anything.southern'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-southern=cli_anything.southern:cli']},
)
