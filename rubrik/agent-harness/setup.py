from setuptools import setup
setup(
    name='cli-anything-rubrik',
    version='1.0.0',
    packages=['cli_anything.rubrik'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rubrik=cli_anything.rubrik:cli']},
)
