from setuptools import setup
setup(
    name='cli-anything-child',
    version='1.0.0',
    packages=['cli_anything.child'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-child=cli_anything.child:cli']},
)
