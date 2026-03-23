from setuptools import setup
setup(
    name='cli-anything-diskspd',
    version='1.0.0',
    packages=['cli_anything.diskspd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-diskspd=cli_anything.diskspd:cli']},
)
