from setuptools import setup
setup(
    name='cli-anything-apache_tajo',
    version='1.0.0',
    packages=['cli_anything.apache_tajo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_tajo=cli_anything.apache_tajo:cli']},
)
