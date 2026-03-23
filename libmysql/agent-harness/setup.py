from setuptools import setup
setup(
    name='cli-anything-libmysql',
    version='1.0.0',
    packages=['cli_anything.libmysql'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-libmysql=cli_anything.libmysql:cli']},
)
