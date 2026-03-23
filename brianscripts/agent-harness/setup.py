from setuptools import setup
setup(
    name='cli-anything-brianscripts',
    version='1.0.0',
    packages=['cli_anything.brianscripts'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-brianscripts=cli_anything.brianscripts:cli']},
)
