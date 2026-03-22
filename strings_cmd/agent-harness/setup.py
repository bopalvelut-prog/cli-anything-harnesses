from setuptools import setup
setup(
    name='cli-anything-strings_cmd',
    version='1.0.0',
    packages=['cli_anything.strings_cmd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-strings_cmd=cli_anything.strings_cmd:cli']},
)
