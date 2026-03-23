from setuptools import setup
setup(
    name='cli-anything-credit',
    version='1.0.0',
    packages=['cli_anything.credit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-credit=cli_anything.credit:cli']},
)
