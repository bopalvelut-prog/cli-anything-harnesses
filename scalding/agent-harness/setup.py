from setuptools import setup
setup(
    name='cli-anything-scalding',
    version='1.0.0',
    packages=['cli_anything.scalding'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scalding=cli_anything.scalding:cli']},
)
