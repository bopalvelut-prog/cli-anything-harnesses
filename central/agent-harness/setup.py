from setuptools import setup
setup(
    name='cli-anything-central',
    version='1.0.0',
    packages=['cli_anything.central'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-central=cli_anything.central:cli']},
)
