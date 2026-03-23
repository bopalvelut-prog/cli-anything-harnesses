from setuptools import setup
setup(
    name='cli-anything-mta',
    version='1.0.0',
    packages=['cli_anything.mta'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mta=cli_anything.mta:cli']},
)
