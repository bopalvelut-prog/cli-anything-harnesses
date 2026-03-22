from setuptools import setup
setup(
    name='cli-anything-svn',
    version='1.0.0',
    packages=['cli_anything.svn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-svn=cli_anything.svn:cli']},
)
