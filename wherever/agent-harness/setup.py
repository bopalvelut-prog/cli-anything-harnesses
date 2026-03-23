from setuptools import setup
setup(
    name='cli-anything-wherever',
    version='1.0.0',
    packages=['cli_anything.wherever'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wherever=cli_anything.wherever:cli']},
)
