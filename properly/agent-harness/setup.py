from setuptools import setup
setup(
    name='cli-anything-properly',
    version='1.0.0',
    packages=['cli_anything.properly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-properly=cli_anything.properly:cli']},
)
