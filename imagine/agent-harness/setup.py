from setuptools import setup
setup(
    name='cli-anything-imagine',
    version='1.0.0',
    packages=['cli_anything.imagine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-imagine=cli_anything.imagine:cli']},
)
