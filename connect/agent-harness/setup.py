from setuptools import setup
setup(
    name='cli-anything-connect',
    version='1.0.0',
    packages=['cli_anything.connect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-connect=cli_anything.connect:cli']},
)
