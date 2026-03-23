from setuptools import setup
setup(
    name='cli-anything-institution',
    version='1.0.0',
    packages=['cli_anything.institution'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-institution=cli_anything.institution:cli']},
)
