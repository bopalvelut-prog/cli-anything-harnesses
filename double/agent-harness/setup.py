from setuptools import setup
setup(
    name='cli-anything-double',
    version='1.0.0',
    packages=['cli_anything.double'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-double=cli_anything.double:cli']},
)
