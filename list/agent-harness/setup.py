from setuptools import setup
setup(
    name='cli-anything-list',
    version='1.0.0',
    packages=['cli_anything.list'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-list=cli_anything.list:cli']},
)
