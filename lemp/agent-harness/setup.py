from setuptools import setup
setup(
    name='cli-anything-lemp',
    version='1.0.0',
    packages=['cli_anything.lemp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lemp=cli_anything.lemp:cli']},
)
