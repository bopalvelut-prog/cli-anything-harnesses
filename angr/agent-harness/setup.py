from setuptools import setup
setup(
    name='cli-anything-angr',
    version='1.0.0',
    packages=['cli_anything.angr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-angr=cli_anything.angr:cli']},
)
