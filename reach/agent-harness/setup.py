from setuptools import setup
setup(
    name='cli-anything-reach',
    version='1.0.0',
    packages=['cli_anything.reach'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reach=cli_anything.reach:cli']},
)
