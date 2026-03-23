from setuptools import setup
setup(
    name='cli-anything-lighttpd',
    version='1.0.0',
    packages=['cli_anything.lighttpd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lighttpd=cli_anything.lighttpd:cli']},
)
