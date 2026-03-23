from setuptools import setup
setup(
    name='cli-anything-discovery',
    version='1.0.0',
    packages=['cli_anything.discovery'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-discovery=cli_anything.discovery:cli']},
)
