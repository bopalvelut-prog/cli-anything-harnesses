from setuptools import setup
setup(
    name='cli-anything-httpd',
    version='1.0.0',
    packages=['cli_anything.httpd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-httpd=cli_anything.httpd:cli']},
)
