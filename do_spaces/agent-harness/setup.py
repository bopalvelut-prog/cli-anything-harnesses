from setuptools import setup
setup(
    name='cli-anything-do_spaces',
    version='1.0.0',
    packages=['cli_anything.do_spaces'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-do_spaces=cli_anything.do_spaces:cli']},
)
