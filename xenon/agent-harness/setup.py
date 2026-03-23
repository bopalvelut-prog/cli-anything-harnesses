from setuptools import setup
setup(
    name='cli-anything-xenon',
    version='1.0.0',
    packages=['cli_anything.xenon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xenon=cli_anything.xenon:cli']},
)
