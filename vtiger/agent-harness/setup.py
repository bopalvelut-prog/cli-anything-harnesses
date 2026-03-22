from setuptools import setup
setup(
    name='cli-anything-vtiger',
    version='1.0.0',
    packages=['cli_anything.vtiger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vtiger=cli_anything.vtiger:cli']},
)
