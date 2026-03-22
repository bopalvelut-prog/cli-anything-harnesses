from setuptools import setup
setup(
    name='cli-anything-mysql_admin',
    version='1.0.0',
    packages=['cli_anything.mysql_admin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mysql_admin=cli_anything.mysql_admin:cli']},
)
