from setuptools import setup
setup(
    name='cli-anything-apache_qpid',
    version='1.0.0',
    packages=['cli_anything.apache_qpid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_qpid=cli_anything.apache_qpid:cli']},
)
