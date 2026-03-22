from setuptools import setup
setup(
    name='cli-anything-nordpass',
    version='1.0.0',
    packages=['cli_anything.nordpass'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nordpass=cli_anything.nordpass:cli']},
)
