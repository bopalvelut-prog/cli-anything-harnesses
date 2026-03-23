from setuptools import setup
setup(
    name='cli-anything-app_5771',
    version='1.0.0',
    packages=['cli_anything.app_5771'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_5771=cli_anything.app_5771:cli']},
)
