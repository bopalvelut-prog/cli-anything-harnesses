from setuptools import setup
setup(
    name='cli-anything-hire',
    version='1.0.0',
    packages=['cli_anything.hire'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hire=cli_anything.hire:cli']},
)
