from setuptools import setup
setup(
    name='cli-anything-confluence',
    version='1.0.0',
    packages=['cli_anything.confluence'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-confluence=cli_anything.confluence:cli']},
)
