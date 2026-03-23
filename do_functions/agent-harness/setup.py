from setuptools import setup
setup(
    name='cli-anything-do_functions',
    version='1.0.0',
    packages=['cli_anything.do_functions'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-do_functions=cli_anything.do_functions:cli']},
)
