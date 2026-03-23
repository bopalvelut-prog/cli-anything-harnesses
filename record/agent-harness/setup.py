from setuptools import setup
setup(
    name='cli-anything-record',
    version='1.0.0',
    packages=['cli_anything.record'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-record=cli_anything.record:cli']},
)
