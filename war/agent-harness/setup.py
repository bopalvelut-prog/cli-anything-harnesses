from setuptools import setup
setup(
    name='cli-anything-war',
    version='1.0.0',
    packages=['cli_anything.war'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-war=cli_anything.war:cli']},
)
