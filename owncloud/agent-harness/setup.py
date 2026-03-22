from setuptools import setup
setup(
    name='cli-anything-owncloud',
    version='1.0.0',
    packages=['cli_anything.owncloud'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-owncloud=cli_anything.owncloud:cli']},
)
