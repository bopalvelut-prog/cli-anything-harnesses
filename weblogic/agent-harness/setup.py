from setuptools import setup
setup(
    name='cli-anything-weblogic',
    version='1.0.0',
    packages=['cli_anything.weblogic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-weblogic=cli_anything.weblogic:cli']},
)
