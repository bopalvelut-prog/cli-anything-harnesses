from setuptools import setup
setup(
    name='cli-anything-r',
    version='1.0.0',
    packages=['cli_anything.r'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-r=cli_anything.r:cli']},
)
