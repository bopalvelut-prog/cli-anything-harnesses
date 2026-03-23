from setuptools import setup
setup(
    name='cli-anything-contact',
    version='1.0.0',
    packages=['cli_anything.contact'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-contact=cli_anything.contact:cli']},
)
