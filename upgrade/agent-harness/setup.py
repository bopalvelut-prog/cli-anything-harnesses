from setuptools import setup
setup(
    name='cli-anything-upgrade',
    version='1.0.0',
    packages=['cli_anything.upgrade'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-upgrade=cli_anything.upgrade:cli']},
)
