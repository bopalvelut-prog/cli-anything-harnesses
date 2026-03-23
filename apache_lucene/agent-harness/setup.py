from setuptools import setup
setup(
    name='cli-anything-apache_lucene',
    version='1.0.0',
    packages=['cli_anything.apache_lucene'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_lucene=cli_anything.apache_lucene:cli']},
)
