from setuptools import setup
setup(
    name='cli-anything-trail',
    version='1.0.0',
    packages=['cli_anything.trail'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trail=cli_anything.trail:cli']},
)
