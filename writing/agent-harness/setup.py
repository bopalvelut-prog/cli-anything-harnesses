from setuptools import setup
setup(
    name='cli-anything-writing',
    version='1.0.0',
    packages=['cli_anything.writing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-writing=cli_anything.writing:cli']},
)
