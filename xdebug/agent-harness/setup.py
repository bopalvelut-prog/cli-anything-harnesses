from setuptools import setup
setup(
    name='cli-anything-xdebug',
    version='1.0.0',
    packages=['cli_anything.xdebug'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xdebug=cli_anything.xdebug:cli']},
)
