from setuptools import setup
setup(
    name='cli-anything-google',
    version='1.0.0',
    packages=['cli_anything.google'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-google=cli_anything.google:cli']},
)
