from setuptools import setup
setup(
    name='cli-anything-configcat',
    version='1.0.0',
    packages=['cli_anything.configcat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-configcat=cli_anything.configcat:cli']},
)
