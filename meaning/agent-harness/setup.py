from setuptools import setup
setup(
    name='cli-anything-meaning',
    version='1.0.0',
    packages=['cli_anything.meaning'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-meaning=cli_anything.meaning:cli']},
)
