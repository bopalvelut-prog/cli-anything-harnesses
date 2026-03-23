from setuptools import setup
setup(
    name='cli-anything-protection',
    version='1.0.0',
    packages=['cli_anything.protection'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-protection=cli_anything.protection:cli']},
)
