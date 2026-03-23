from setuptools import setup
setup(
    name='cli-anything-workflow',
    version='1.0.0',
    packages=['cli_anything.workflow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-workflow=cli_anything.workflow:cli']},
)
