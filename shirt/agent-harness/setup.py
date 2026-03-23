from setuptools import setup
setup(
    name='cli-anything-shirt',
    version='1.0.0',
    packages=['cli_anything.shirt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shirt=cli_anything.shirt:cli']},
)
