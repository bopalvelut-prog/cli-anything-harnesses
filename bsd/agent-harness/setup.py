from setuptools import setup
setup(
    name='cli-anything-bsd',
    version='1.0.0',
    packages=['cli_anything.bsd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bsd=cli_anything.bsd:cli']},
)
