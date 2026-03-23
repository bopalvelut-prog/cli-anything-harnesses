from setuptools import setup
setup(
    name='cli-anything-infinity',
    version='1.0.0',
    packages=['cli_anything.infinity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-infinity=cli_anything.infinity:cli']},
)
