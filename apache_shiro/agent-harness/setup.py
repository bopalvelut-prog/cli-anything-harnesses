from setuptools import setup
setup(
    name='cli-anything-apache_shiro',
    version='1.0.0',
    packages=['cli_anything.apache_shiro'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_shiro=cli_anything.apache_shiro:cli']},
)
