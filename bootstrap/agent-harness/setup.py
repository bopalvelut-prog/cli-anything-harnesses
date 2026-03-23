from setuptools import setup
setup(
    name='cli-anything-bootstrap',
    version='1.0.0',
    packages=['cli_anything.bootstrap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bootstrap=cli_anything.bootstrap:cli']},
)
