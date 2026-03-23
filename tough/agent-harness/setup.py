from setuptools import setup
setup(
    name='cli-anything-tough',
    version='1.0.0',
    packages=['cli_anything.tough'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tough=cli_anything.tough:cli']},
)
