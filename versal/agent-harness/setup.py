from setuptools import setup
setup(
    name='cli-anything-versal',
    version='1.0.0',
    packages=['cli_anything.versal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-versal=cli_anything.versal:cli']},
)
