from setuptools import setup
setup(
    name='cli-anything-asterisk',
    version='1.0.0',
    packages=['cli_anything.asterisk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-asterisk=cli_anything.asterisk:cli']},
)
