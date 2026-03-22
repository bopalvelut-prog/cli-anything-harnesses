from setuptools import setup
setup(
    name='cli-anything-typeform',
    version='1.0.0',
    packages=['cli_anything.typeform'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-typeform=cli_anything.typeform:cli']},
)
