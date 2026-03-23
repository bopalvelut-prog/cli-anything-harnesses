from setuptools import setup
setup(
    name='cli-anything-possibly',
    version='1.0.0',
    packages=['cli_anything.possibly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-possibly=cli_anything.possibly:cli']},
)
