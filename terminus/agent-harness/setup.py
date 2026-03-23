from setuptools import setup
setup(
    name='cli-anything-terminus',
    version='1.0.0',
    packages=['cli_anything.terminus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-terminus=cli_anything.terminus:cli']},
)
