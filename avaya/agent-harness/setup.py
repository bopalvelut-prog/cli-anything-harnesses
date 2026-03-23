from setuptools import setup
setup(
    name='cli-anything-avaya',
    version='1.0.0',
    packages=['cli_anything.avaya'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-avaya=cli_anything.avaya:cli']},
)
