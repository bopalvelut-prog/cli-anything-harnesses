from setuptools import setup
setup(
    name='cli-anything-build',
    version='1.0.0',
    packages=['cli_anything.build'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-build=cli_anything.build:cli']},
)
