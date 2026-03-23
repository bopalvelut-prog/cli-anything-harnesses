from setuptools import setup
setup(
    name='cli-anything-apache_struts',
    version='1.0.0',
    packages=['cli_anything.apache_struts'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_struts=cli_anything.apache_struts:cli']},
)
