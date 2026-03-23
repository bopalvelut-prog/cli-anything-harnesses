from setuptools import setup
setup(
    name='cli-anything-city',
    version='1.0.0',
    packages=['cli_anything.city'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-city=cli_anything.city:cli']},
)
