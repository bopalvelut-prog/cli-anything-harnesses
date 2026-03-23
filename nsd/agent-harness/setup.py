from setuptools import setup
setup(
    name='cli-anything-nsd',
    version='1.0.0',
    packages=['cli_anything.nsd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nsd=cli_anything.nsd:cli']},
)
