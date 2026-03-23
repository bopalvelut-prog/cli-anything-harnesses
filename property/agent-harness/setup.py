from setuptools import setup
setup(
    name='cli-anything-property',
    version='1.0.0',
    packages=['cli_anything.property'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-property=cli_anything.property:cli']},
)
