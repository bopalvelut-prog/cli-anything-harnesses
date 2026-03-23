from setuptools import setup
setup(
    name='cli-anything-push',
    version='1.0.0',
    packages=['cli_anything.push'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-push=cli_anything.push:cli']},
)
