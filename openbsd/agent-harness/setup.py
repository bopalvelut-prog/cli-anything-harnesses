from setuptools import setup
setup(
    name='cli-anything-openbsd',
    version='1.0.0',
    packages=['cli_anything.openbsd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-openbsd=cli_anything.openbsd:cli']},
)
