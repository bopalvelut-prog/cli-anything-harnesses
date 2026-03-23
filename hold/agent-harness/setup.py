from setuptools import setup
setup(
    name='cli-anything-hold',
    version='1.0.0',
    packages=['cli_anything.hold'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hold=cli_anything.hold:cli']},
)
