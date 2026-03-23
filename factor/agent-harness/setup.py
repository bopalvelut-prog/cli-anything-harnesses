from setuptools import setup
setup(
    name='cli-anything-factor',
    version='1.0.0',
    packages=['cli_anything.factor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-factor=cli_anything.factor:cli']},
)
