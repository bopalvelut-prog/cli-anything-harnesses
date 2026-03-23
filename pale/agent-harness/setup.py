from setuptools import setup
setup(
    name='cli-anything-pale',
    version='1.0.0',
    packages=['cli_anything.pale'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pale=cli_anything.pale:cli']},
)
