from setuptools import setup
setup(
    name='cli-anything-autoupdate',
    version='1.0.0',
    packages=['cli_anything.autoupdate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autoupdate=cli_anything.autoupdate:cli']},
)
