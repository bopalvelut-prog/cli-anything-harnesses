from setuptools import setup
setup(
    name='cli-anything-town',
    version='1.0.0',
    packages=['cli_anything.town'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-town=cli_anything.town:cli']},
)
