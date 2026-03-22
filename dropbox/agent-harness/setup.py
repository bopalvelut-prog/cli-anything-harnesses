from setuptools import setup
setup(
    name='cli-anything-dropbox',
    version='1.0.0',
    packages=['cli_anything.dropbox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dropbox=cli_anything.dropbox:cli']},
)
