from setuptools import setup
setup(
    name='cli-anything-contentful',
    version='1.0.0',
    packages=['cli_anything.contentful'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-contentful=cli_anything.contentful:cli']},
)
