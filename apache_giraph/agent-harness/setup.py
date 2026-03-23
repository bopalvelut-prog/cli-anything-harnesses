from setuptools import setup
setup(
    name='cli-anything-apache_giraph',
    version='1.0.0',
    packages=['cli_anything.apache_giraph'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_giraph=cli_anything.apache_giraph:cli']},
)
