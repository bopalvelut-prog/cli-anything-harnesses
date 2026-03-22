from setuptools import setup
setup(
    name='cli-anything-wordpress',
    version='1.0.0',
    packages=['cli_anything.wordpress'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wordpress=cli_anything.wordpress:cli']},
)
