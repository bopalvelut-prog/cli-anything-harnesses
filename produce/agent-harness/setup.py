from setuptools import setup
setup(
    name='cli-anything-produce',
    version='1.0.0',
    packages=['cli_anything.produce'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-produce=cli_anything.produce:cli']},
)
