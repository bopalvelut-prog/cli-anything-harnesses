from setuptools import setup
setup(
    name='cli-anything-ward',
    version='1.0.0',
    packages=['cli_anything.ward'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ward=cli_anything.ward:cli']},
)
