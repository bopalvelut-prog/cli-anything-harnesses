from setuptools import setup
setup(
    name='cli-anything-apache_hama',
    version='1.0.0',
    packages=['cli_anything.apache_hama'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_hama=cli_anything.apache_hama:cli']},
)
