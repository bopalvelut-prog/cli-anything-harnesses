from setuptools import setup
setup(
    name='cli-anything-mariadb',
    version='1.0.0',
    packages=['cli_anything.mariadb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mariadb=cli_anything.mariadb:cli']},
)
