from setuptools import setup
setup(
    name='cli-anything-bind',
    version='1.0.0',
    packages=['cli_anything.bind'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bind=cli_anything.bind:cli']},
)
