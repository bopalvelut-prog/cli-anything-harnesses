from setuptools import setup
setup(
    name='cli-anything-regex',
    version='1.0.0',
    packages=['cli_anything.regex'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-regex=cli_anything.regex:cli']},
)
