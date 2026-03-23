from setuptools import setup
setup(
    name='cli-anything-retire',
    version='1.0.0',
    packages=['cli_anything.retire'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-retire=cli_anything.retire:cli']},
)
