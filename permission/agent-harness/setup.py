from setuptools import setup
setup(
    name='cli-anything-permission',
    version='1.0.0',
    packages=['cli_anything.permission'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-permission=cli_anything.permission:cli']},
)
