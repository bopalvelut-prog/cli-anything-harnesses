from setuptools import setup
setup(
    name='cli-anything-busy',
    version='1.0.0',
    packages=['cli_anything.busy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-busy=cli_anything.busy:cli']},
)
