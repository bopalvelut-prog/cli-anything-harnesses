from setuptools import setup
setup(
    name='cli-anything-many',
    version='1.0.0',
    packages=['cli_anything.many'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-many=cli_anything.many:cli']},
)
