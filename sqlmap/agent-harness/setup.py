from setuptools import setup
setup(
    name='cli-anything-sqlmap',
    version='1.0.0',
    packages=['cli_anything.sqlmap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sqlmap=cli_anything.sqlmap:cli']},
)
