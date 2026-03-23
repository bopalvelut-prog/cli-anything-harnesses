from setuptools import setup
setup(
    name='cli-anything-app_1612',
    version='1.0.0',
    packages=['cli_anything.app_1612'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_1612=cli_anything.app_1612:cli']},
)
