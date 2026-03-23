from setuptools import setup
setup(
    name='cli-anything-ceremony',
    version='1.0.0',
    packages=['cli_anything.ceremony'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ceremony=cli_anything.ceremony:cli']},
)
