from setuptools import setup
setup(
    name='cli-anything-relate',
    version='1.0.0',
    packages=['cli_anything.relate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-relate=cli_anything.relate:cli']},
)
