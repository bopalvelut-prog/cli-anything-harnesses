from setuptools import setup
setup(
    name='cli-anything-mocha',
    version='1.0.0',
    packages=['cli_anything.mocha'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mocha=cli_anything.mocha:cli']},
)
