from setuptools import setup
setup(
    name='cli-anything-xsd',
    version='1.0.0',
    packages=['cli_anything.xsd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xsd=cli_anything.xsd:cli']},
)
