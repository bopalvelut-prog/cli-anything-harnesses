from setuptools import setup
setup(
    name='cli-anything-location',
    version='1.0.0',
    packages=['cli_anything.location'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-location=cli_anything.location:cli']},
)
