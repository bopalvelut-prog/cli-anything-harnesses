from setuptools import setup
setup(
    name='cli-anything-keynote',
    version='1.0.0',
    packages=['cli_anything.keynote'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-keynote=cli_anything.keynote:cli']},
)
