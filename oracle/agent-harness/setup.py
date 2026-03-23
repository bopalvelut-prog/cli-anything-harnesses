from setuptools import setup
setup(
    name='cli-anything-oracle',
    version='1.0.0',
    packages=['cli_anything.oracle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-oracle=cli_anything.oracle:cli']},
)
