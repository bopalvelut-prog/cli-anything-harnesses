from setuptools import setup
setup(
    name='cli-anything-derby',
    version='1.0.0',
    packages=['cli_anything.derby'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-derby=cli_anything.derby:cli']},
)
