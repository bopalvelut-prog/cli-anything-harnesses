from setuptools import setup
setup(
    name='cli-anything-applinks',
    version='1.0.0',
    packages=['cli_anything.applinks'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-applinks=cli_anything.applinks:cli']},
)
