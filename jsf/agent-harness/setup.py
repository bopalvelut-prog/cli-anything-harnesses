from setuptools import setup
setup(
    name='cli-anything-jsf',
    version='1.0.0',
    packages=['cli_anything.jsf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jsf=cli_anything.jsf:cli']},
)
