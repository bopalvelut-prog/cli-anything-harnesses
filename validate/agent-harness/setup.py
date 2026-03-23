from setuptools import setup
setup(
    name='cli-anything-validate',
    version='1.0.0',
    packages=['cli_anything.validate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-validate=cli_anything.validate:cli']},
)
