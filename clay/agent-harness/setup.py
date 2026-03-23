from setuptools import setup
setup(
    name='cli-anything-clay',
    version='1.0.0',
    packages=['cli_anything.clay'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clay=cli_anything.clay:cli']},
)
