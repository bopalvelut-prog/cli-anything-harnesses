from setuptools import setup
setup(
    name='cli-anything-nginx_unit',
    version='1.0.0',
    packages=['cli_anything.nginx_unit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nginx_unit=cli_anything.nginx_unit:cli']},
)
