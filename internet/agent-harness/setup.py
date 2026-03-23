from setuptools import setup
setup(
    name='cli-anything-internet',
    version='1.0.0',
    packages=['cli_anything.internet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-internet=cli_anything.internet:cli']},
)
