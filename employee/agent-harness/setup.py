from setuptools import setup
setup(
    name='cli-anything-employee',
    version='1.0.0',
    packages=['cli_anything.employee'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-employee=cli_anything.employee:cli']},
)
