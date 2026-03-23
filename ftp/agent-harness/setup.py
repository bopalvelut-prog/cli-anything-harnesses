from setuptools import setup
setup(
    name='cli-anything-ftp',
    version='1.0.0',
    packages=['cli_anything.ftp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ftp=cli_anything.ftp:cli']},
)
