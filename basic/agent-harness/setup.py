from setuptools import setup
setup(
    name='cli-anything-basic',
    version='1.0.0',
    packages=['cli_anything.basic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-basic=cli_anything.basic:cli']},
)
