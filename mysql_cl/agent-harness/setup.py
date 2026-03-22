from setuptools import setup
setup(
    name='cli-anything-mysql_cl',
    version='1.0.0',
    packages=['cli_anything.mysql_cl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mysql_cl=cli_anything.mysql_cl:cli']},
)
