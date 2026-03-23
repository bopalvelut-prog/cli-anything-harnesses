from setuptools import setup
setup(
    name='cli-anything-discover',
    version='1.0.0',
    packages=['cli_anything.discover'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-discover=cli_anything.discover:cli']},
)
