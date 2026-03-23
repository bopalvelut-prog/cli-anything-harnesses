from setuptools import setup
setup(
    name='cli-anything-terrible',
    version='1.0.0',
    packages=['cli_anything.terrible'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-terrible=cli_anything.terrible:cli']},
)
