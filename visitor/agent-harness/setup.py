from setuptools import setup
setup(
    name='cli-anything-visitor',
    version='1.0.0',
    packages=['cli_anything.visitor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-visitor=cli_anything.visitor:cli']},
)
