from setuptools import setup
setup(
    name='cli-anything-netcat',
    version='1.0.0',
    packages=['cli_anything.netcat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-netcat=cli_anything.netcat:cli']},
)
