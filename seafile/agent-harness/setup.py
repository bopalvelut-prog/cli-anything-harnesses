from setuptools import setup
setup(
    name='cli-anything-seafile',
    version='1.0.0',
    packages=['cli_anything.seafile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-seafile=cli_anything.seafile:cli']},
)
