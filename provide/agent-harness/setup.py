from setuptools import setup
setup(
    name='cli-anything-provide',
    version='1.0.0',
    packages=['cli_anything.provide'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-provide=cli_anything.provide:cli']},
)
