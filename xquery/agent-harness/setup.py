from setuptools import setup
setup(
    name='cli-anything-xquery',
    version='1.0.0',
    packages=['cli_anything.xquery'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xquery=cli_anything.xquery:cli']},
)
