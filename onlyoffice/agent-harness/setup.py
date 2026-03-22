from setuptools import setup
setup(
    name='cli-anything-onlyoffice',
    version='1.0.0',
    packages=['cli_anything.onlyoffice'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-onlyoffice=cli_anything.onlyoffice:cli']},
)
