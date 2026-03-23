from setuptools import setup
setup(
    name='cli-anything-app_2181',
    version='1.0.0',
    packages=['cli_anything.app_2181'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_2181=cli_anything.app_2181:cli']},
)
