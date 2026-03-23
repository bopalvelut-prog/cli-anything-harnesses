from setuptools import setup
setup(
    name='cli-anything-formula',
    version='1.0.0',
    packages=['cli_anything.formula'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-formula=cli_anything.formula:cli']},
)
