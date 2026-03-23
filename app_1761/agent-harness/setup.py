from setuptools import setup
setup(
    name='cli-anything-app_1761',
    version='1.0.0',
    packages=['cli_anything.app_1761'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_1761=cli_anything.app_1761:cli']},
)
