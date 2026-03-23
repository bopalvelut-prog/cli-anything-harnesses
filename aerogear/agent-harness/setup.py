from setuptools import setup
setup(
    name='cli-anything-aerogear',
    version='1.0.0',
    packages=['cli_anything.aerogear'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aerogear=cli_anything.aerogear:cli']},
)
