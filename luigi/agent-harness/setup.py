from setuptools import setup
setup(
    name='cli-anything-luigi',
    version='1.0.0',
    packages=['cli_anything.luigi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-luigi=cli_anything.luigi:cli']},
)
