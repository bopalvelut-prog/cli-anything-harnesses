from setuptools import setup
setup(
    name='cli-anything-slash',
    version='1.0.0',
    packages=['cli_anything.slash'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slash=cli_anything.slash:cli']},
)
