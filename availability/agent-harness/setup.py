from setuptools import setup
setup(
    name='cli-anything-availability',
    version='1.0.0',
    packages=['cli_anything.availability'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-availability=cli_anything.availability:cli']},
)
