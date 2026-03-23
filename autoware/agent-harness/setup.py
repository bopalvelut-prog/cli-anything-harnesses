from setuptools import setup
setup(
    name='cli-anything-autoware',
    version='1.0.0',
    packages=['cli_anything.autoware'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autoware=cli_anything.autoware:cli']},
)
