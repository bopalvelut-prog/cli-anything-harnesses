from setuptools import setup
setup(
    name='cli-anything-pidgin',
    version='1.0.0',
    packages=['cli_anything.pidgin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pidgin=cli_anything.pidgin:cli']},
)
